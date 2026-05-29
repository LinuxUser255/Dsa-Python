#!/usr/bin/env python3
"""Evaluate pending predictions against actual market outcomes.

This script:
1. Scans ALL prediction JSON files across ALL pairs (BTC, ETH, XMR, SOL, etc.)
2. Identifies predictions where target_time has passed but evaluation is null
3. Fetches the actual price at target_time from Kraken
4. Scores the prediction (direction accuracy, range accuracy)
5. Writes the evaluation block back to the JSON file

Usage:
    python scripts/evaluate.py              # Evaluate ALL pending predictions (all pairs, Grok)
    python scripts/evaluate.py --provider claude  # Evaluate Claude predictions
    python scripts/evaluate.py --dry-run    # Show what would be evaluated
    python scripts/evaluate.py --pair BTC/USD   # Evaluate only BTC/USD

Recommended: Run via cron every 15 minutes:
    */15 * * * * cd /path/to/CryptoAnalysisBot && python3 scripts/evaluate.py >> logs/evaluate.log 2>&1
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.kraken_client import fetch_ticker
from src.config import CryptoPair, CLASSIFY_K, CLASSIFY_K_BY_HORIZON
from src.db import PROVIDER_DIRS


# Provider-specific directories
PROVIDER_QUERIES_DIRS = {
    "grok": Path(__file__).parent.parent / "data" / "queries",
    "claude": Path(__file__).parent.parent / "data" / "queries_claude",
}


def parse_iso_datetime(ts: str) -> datetime:
    """Parse ISO datetime string to timezone-aware datetime."""
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return datetime.fromisoformat(ts)


def find_pending_predictions(
    pair_filter: Optional[str] = None,
    horizon_filter: Optional[str] = None,
    provider: str = "grok",
) -> List[Path]:
    """Find all prediction files that need evaluation across ALL horizons and pairs.
    
    A prediction is pending if:
    - target_time exists and has passed
    - evaluation is null or missing
    
    Directory structure:
        data/queries/{horizon}/{pair}/*.json
        e.g., data/queries/1h/BTC_USD/2025-11-29_00-00_ET.json
    
    Args:
        pair_filter: Optional pair to filter (e.g., "BTC/USD"). 
                     If None, scans ALL pairs.
        horizon_filter: Optional horizon to filter (e.g., "1h", "3h", "6h").
                        If None, scans ALL horizons.
    
    Returns:
        List of paths to JSON files needing evaluation.
    """
    pending = []
    now = datetime.now(timezone.utc)
    
    queries_dir = PROVIDER_QUERIES_DIRS.get(provider, PROVIDER_QUERIES_DIRS["grok"])
    
    if not queries_dir.exists():
        return pending
    
    # Determine which horizon directories to scan
    if horizon_filter:
        horizon_dirs = [queries_dir / horizon_filter]
    else:
        # Scan all horizon directories (1h, 3h, 6h, etc.)
        horizon_dirs = [d for d in queries_dir.iterdir() if d.is_dir()]
    
    for horizon_dir in horizon_dirs:
        if not horizon_dir.exists():
            continue
        
        # Determine which pair directories to scan within this horizon
        if pair_filter:
            pair_slug = CryptoPair.to_slug(pair_filter)
            pair_dirs = [horizon_dir / pair_slug]
        else:
            # Scan ALL pair directories within this horizon
            pair_dirs = [d for d in horizon_dir.iterdir() if d.is_dir()]
        
        for pair_dir in pair_dirs:
            if not pair_dir.exists():
                continue
                
            for json_file in pair_dir.glob("*.json"):
                # Skip symlinks (like latest.json)
                if json_file.is_symlink():
                    continue
                
                try:
                    with json_file.open("r", encoding="utf-8") as f:
                        data = json.load(f)
                    
                    # Check if already evaluated
                    if data.get("evaluation") is not None:
                        continue
                    
                    # Check if target_time exists and has passed
                    target_time_str = data.get("target_time")
                    if not target_time_str:
                        continue
                    
                    target_time = parse_iso_datetime(target_time_str)
                    if target_time <= now:
                        pending.append(json_file)
                        
                except (json.JSONDecodeError, KeyError, ValueError):
                    # Skip malformed files
                    continue
    
    return sorted(pending)


def fetch_price_at_target(pair: str) -> Optional[float]:
    """Fetch current price for a pair from Kraken.
    
    Note: Kraken doesn't provide historical tick data via public API,
    so we fetch the current price. For best accuracy, run the evaluator
    shortly after target_time passes.
    
    Args:
        pair: Trading pair (e.g., "BTC/USD", "ETH/USD", "XMR/USD")
    
    Returns:
        Current price or None if fetch fails.
    """
    try:
        ticker = fetch_ticker(pair)
        return ticker.get("last_price")
    except Exception:
        return None


def evaluate_prediction(pred_data: Dict[str, Any], actual_price: float) -> Dict[str, Any]:
    """Score a prediction against actual market outcome.
    
    Args:
        pred_data: The full prediction JSON data
        actual_price: The actual price at target time
    
    Returns:
        Evaluation dict with scores and metrics.
    """
    now = datetime.now(timezone.utc)
    
    # Extract prediction details
    prediction = pred_data.get("prediction_next_day", {})
    market_snapshot = pred_data.get("market_snapshot", {})
    
    price_at_prediction = market_snapshot.get("current_price", 0)
    direction_bias = prediction.get("direction_bias", "uncertain")
    confidence = prediction.get("confidence", 0)
    expected_range = prediction.get("expected_move_pct_range", {})
    expected_low = expected_range.get("low", -999)
    expected_high = expected_range.get("high", 999)
    
    # Calculate actual move
    if price_at_prediction > 0:
        actual_move_pct = ((actual_price / price_at_prediction) - 1) * 100
    else:
        actual_move_pct = 0
    
    # Evaluate direction accuracy
    direction_correct: Optional[bool] = None
    if direction_bias == "up":
        direction_correct = actual_move_pct > 0
    elif direction_bias == "down":
        direction_correct = actual_move_pct < 0
    elif direction_bias == "sideways":
        # Sideways is correct if move is relatively small
        # Phase 2A: Use horizon-specific CLASSIFY_K for consistency with LLM prompt
        time_horizon = pred_data.get("time_horizon", "1h")
        classify_k = CLASSIFY_K_BY_HORIZON.get(time_horizon, CLASSIFY_K)
        daily_vol = pred_data.get("indicators", {}).get("daily_vol_pct", 2.0)
        sideways_threshold = daily_vol * classify_k
        direction_correct = abs(actual_move_pct) < sideways_threshold
    # "uncertain" predictions are not scored for direction
    
    # Evaluate range accuracy
    within_range = expected_low <= actual_move_pct <= expected_high
    
    # Compute composite score (0-1)
    # Weights: 50% direction, 30% range, 20% confidence calibration
    score_components = []
    
    if direction_correct is not None:
        score_components.append(("direction", 0.5, 1.0 if direction_correct else 0.0))
    
    score_components.append(("range", 0.3, 1.0 if within_range else 0.0))
    
    # Confidence calibration: reward when high confidence matches correctness
    if direction_correct is not None:
        calibration = confidence if direction_correct else (1 - confidence)
        score_components.append(("calibration", 0.2, calibration))
    
    # Calculate weighted score
    total_weight = sum(w for _, w, _ in score_components)
    if total_weight > 0:
        composite_score = sum(w * s for _, w, s in score_components) / total_weight
    else:
        composite_score = 0.5  # Neutral for uncertain predictions
    
    # Determine outcome label for investors
    if direction_correct is True:
        outcome_label = "CORRECT"
    elif direction_correct is False:
        outcome_label = "INCORRECT"
    else:
        outcome_label = "NOT SCORED"  # uncertain predictions
    
    return {
        "evaluated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "price_at_prediction": price_at_prediction,
        "price_at_target": actual_price,
        "actual_move_pct": round(actual_move_pct, 4),
        "direction_predicted": direction_bias,
        "direction_correct": direction_correct,
        "expected_range_low": expected_low,
        "expected_range_high": expected_high,
        "within_range": within_range,
        "confidence": confidence,
        "composite_score": round(composite_score, 4),
        "outcome_label": outcome_label,
    }


def process_prediction(json_path: Path, dry_run: bool = False) -> Optional[Dict[str, Any]]:
    """Evaluate a single prediction file.
    
    Args:
        json_path: Path to the prediction JSON file
        dry_run: If True, don't modify the file
    
    Returns:
        Evaluation dict if successful, None otherwise.
    """
    try:
        with json_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        
        pair = data.get("pair", "BTC/USD")
        target_time = data.get("target_time", "unknown")
        
        print(f"  Evaluating: {json_path.name}")
        print(f"    Pair: {pair}")
        print(f"    Target time: {target_time}")
        
        # Fetch actual price
        actual_price = fetch_price_at_target(pair)
        if actual_price is None:
            print(f"    ERROR: Could not fetch price for {pair}")
            return None
        
        print(f"    Actual price: ${actual_price:,.2f}")
        
        # Evaluate
        evaluation = evaluate_prediction(data, actual_price)
        
        print(f"    Direction: {evaluation['direction_predicted']} -> {evaluation['outcome_label']}")
        print(f"    Move: {evaluation['actual_move_pct']:+.2f}%")
        print(f"    Score: {evaluation['composite_score']:.2f}")
        
        if not dry_run:
            # Write evaluation back to file
            data["evaluation"] = evaluation
            with json_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"    ✓ Saved evaluation")
        else:
            print(f"    (dry run - not saved)")
        
        return evaluation
        
    except Exception as e:
        print(f"    ERROR: {e}")
        return None


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate pending cryptocurrency predictions against actual outcomes.",
        epilog="By default, evaluates ALL horizons (1h, 3h, 6h, etc.) and ALL pairs."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be evaluated without modifying files",
    )
    parser.add_argument(
        "--pair",
        type=str,
        default=None,
        help="Evaluate only predictions for a specific pair (e.g., BTC/USD). "
             "If omitted, evaluates ALL pairs.",
    )
    parser.add_argument(
        "--horizon",
        type=str,
        default=None,
        help="Evaluate only predictions for a specific horizon (e.g., 1h, 3h, 6h). "
             "If omitted, evaluates ALL horizons.",
    )
    parser.add_argument(
        "--generate-reports",
        action="store_true",
        help="After evaluation, auto-generate accuracy reports for all horizons with data.",
    )
    parser.add_argument(
        "--provider",
        type=str,
        default="grok",
        choices=["grok", "claude"],
        help="LLM provider to evaluate (default: grok)",
    )
    args = parser.parse_args()
    
    print("=" * 60)
    print(f"  CryptoAnalysisBot - Prediction Evaluator ({args.provider.upper()})")
    print("=" * 60)
    
    if args.dry_run:
        print("(DRY RUN - no files will be modified)")
    
    print(f"(Provider: {args.provider})")
    
    filters = []
    if args.horizon:
        filters.append(f"horizon={args.horizon}")
    if args.pair:
        filters.append(f"pair={args.pair}")
    
    if filters:
        print(f"(Filtering: {', '.join(filters)})")
    else:
        print("(Scanning ALL horizons and ALL pairs)")
    
    print()
    
    # Find pending predictions across all horizons and pairs
    pending = find_pending_predictions(args.pair, args.horizon, args.provider)
    
    if not pending:
        print("No pending predictions to evaluate.")
        print("(Predictions need target_time in the past and evaluation=null)")
        return
    
    # Group by horizon and pair for display
    by_horizon_pair: Dict[str, Dict[str, List[Path]]] = {}
    for p in pending:
        pair_slug = p.parent.name
        horizon = p.parent.parent.name
        by_horizon_pair.setdefault(horizon, {}).setdefault(pair_slug, []).append(p)
    
    print(f"Found {len(pending)} prediction(s) to evaluate:")
    for horizon, pairs in sorted(by_horizon_pair.items()):
        print(f"  [{horizon}]")
        for pair_slug, files in sorted(pairs.items()):
            print(f"    {pair_slug}: {len(files)} file(s)")
    print()
    
    # Process each prediction
    results = {
        "evaluated": 0,
        "correct": 0,
        "incorrect": 0,
        "not_scored": 0,
        "failed": 0,
        "by_horizon": {},
    }
    
    for json_path in pending:
        pair_slug = json_path.parent.name
        horizon = json_path.parent.parent.name
        key = f"{horizon}/{pair_slug}"
        evaluation = process_prediction(json_path, args.dry_run)
        
        # Track per-horizon/pair stats
        if key not in results["by_horizon"]:
            results["by_horizon"][key] = {"correct": 0, "incorrect": 0, "not_scored": 0}
        
        if evaluation:
            results["evaluated"] += 1
            if evaluation["outcome_label"] == "CORRECT":
                results["correct"] += 1
                results["by_horizon"][key]["correct"] += 1
            elif evaluation["outcome_label"] == "INCORRECT":
                results["incorrect"] += 1
                results["by_horizon"][key]["incorrect"] += 1
            else:
                results["not_scored"] += 1
                results["by_horizon"][key]["not_scored"] += 1
        else:
            results["failed"] += 1
        
        print()
    
    # Summary
    print("=" * 60)
    print("  Summary")
    print("=" * 60)
    print(f"  Total Evaluated: {results['evaluated']}")
    print(f"  Correct:         {results['correct']}")
    print(f"  Incorrect:       {results['incorrect']}")
    print(f"  Not scored:      {results['not_scored']}")
    print(f"  Failed:          {results['failed']}")
    
    # Overall accuracy
    scored = results["correct"] + results["incorrect"]
    if scored > 0:
        accuracy = results["correct"] / scored * 100
        print(f"\n  Overall Direction Accuracy: {accuracy:.1f}% ({results['correct']}/{scored})")
    
    # Per-horizon/pair breakdown
    if len(results["by_horizon"]) > 1:
        print("\n  Per-Horizon/Pair Breakdown:")
        print("  " + "-" * 40)
        for key, stats in sorted(results["by_horizon"].items()):
            key_scored = stats["correct"] + stats["incorrect"]
            if key_scored > 0:
                key_acc = stats["correct"] / key_scored * 100
                print(f"    {key}: {key_acc:.0f}% ({stats['correct']}/{key_scored})")
            else:
                print(f"    {key}: No scored predictions")
    
    print("=" * 60)
    
    # Generate reports if requested
    if args.generate_reports and results["evaluated"] > 0 and not args.dry_run:
        print()
        print("Generating accuracy reports...")
        import subprocess
        try:
            report_result = subprocess.run(
                [sys.executable, "scripts/accuracy_report.py", "--auto", "--provider", args.provider],
                capture_output=True,
                text=True,
                timeout=120,
            )
            if report_result.returncode == 0:
                print("  \u2713 Reports generated successfully")
            else:
                print(f"  Report generation failed: {report_result.stderr}")
        except Exception as e:
            print(f"  Report generation error: {e}")


if __name__ == "__main__":
    main()
