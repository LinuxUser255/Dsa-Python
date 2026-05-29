from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from pathlib import Path
from typing import Any, Dict, Optional

from .config import CryptoPair


# Map time horizon strings to timedelta
HORIZON_DELTAS = {
    "1h": timedelta(hours=1),
    "2h": timedelta(hours=2),
    "4h": timedelta(hours=4),
    "6h": timedelta(hours=6),
    "12h": timedelta(hours=12),
    "24h": timedelta(hours=24),
}


# Default directory where per-query JSON files will be stored
DEFAULT_BASE_DIR = Path("data") / "queries"

# Provider-specific base directories for A/B testing
PROVIDER_DIRS = {
    "grok": Path("data") / "queries",         # Default (existing)
    "claude": Path("data") / "queries_claude",  # Claude A/B test
}


@dataclass
class QueryRecord:
    """Metadata about a stored query result."""

    path: Path
    timestamp: str


def save_query_result(
    payload: Dict[str, Any],
    base_dir: Optional[Path] = None,
    provider: str = "grok",
) -> QueryRecord:
    """Persist a single inquiry's result as a JSON file.

    Layout (organized by horizon and pair):
        data/queries/{HORIZON}/{PAIR}/YYYY-MM-DD_HH-MM_ET.json       (grok)
        data/queries_claude/{HORIZON}/{PAIR}/YYYY-MM-DD_HH-MM_ET.json (claude)
    
    Args:
        payload: The analysis result dict to save.
        base_dir: Override the base directory (ignores provider if set).
        provider: LLM provider name ("grok" or "claude") for directory selection.
    
    Example:
        data/queries/1h/BTC_USD/2025-11-29_00-00_ET.json
        data/queries_claude/1h/BTC_USD/2025-11-29_00-00_ET.json
    
    Also maintains a per-pair symlink:
        {base}/{HORIZON}/{PAIR}/latest.json -> most recent file
    """
    if base_dir is None:
        base_dir = PROVIDER_DIRS.get(provider, DEFAULT_BASE_DIR)

    # Normalize pair name to canonical format (e.g., XBT/USD -> BTC/USD)
    raw_pair = payload.get("pair", "BTC/USD")
    pair = CryptoPair.normalize(raw_pair)
    pair_slug = CryptoPair.to_slug(pair)
    
    # Get horizon for directory structure
    time_horizon = payload.get("time_horizon", "1h")

    # Directory structure: base/horizon/pair/
    pair_dir = base_dir / time_horizon / pair_slug
    pair_dir.mkdir(parents=True, exist_ok=True)

    # Use readable timestamp (explicit UTC marker)
    ts_dt = datetime.now(timezone.utc)
    # Filename uses ET for user-facing clarity
    ts_readable = ts_dt.astimezone(ZoneInfo("America/New_York")).strftime("%Y-%m-%d_%H-%M_ET")

    filename = f"{ts_readable}.json"
    path = pair_dir / filename

    # Append created_at (UTC) and created_at_et to payload (non-destructive)
    et = ts_dt.astimezone(ZoneInfo("America/New_York"))
    
    # Calculate target evaluation time based on horizon
    horizon_delta = HORIZON_DELTAS.get(time_horizon, timedelta(hours=1))
    target_dt = ts_dt + horizon_delta
    target_et = target_dt.astimezone(ZoneInfo("America/New_York"))
    
    enriched = {
        **payload,
        "pair": pair,  # Store normalized pair name
        "provider": provider,  # Track which LLM made this prediction
        "created_at": ts_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "created_at_et": et.isoformat(timespec="seconds"),
        "created_at_utc": ts_dt.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "created_at_et_formatted": f"{et.strftime('%Y-%m-%d %I:%M:%S %p ET')} ({ts_dt.strftime('%Y-%m-%d %H:%M:%S UTC')})",
        # Target time for accuracy evaluation
        "target_time": target_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "target_time_et": target_et.isoformat(timespec="seconds"),
        "target_time_formatted": f"{target_et.strftime('%Y-%m-%d %I:%M:%S %p ET')} ({target_dt.strftime('%Y-%m-%d %H:%M:%S UTC')})",
        # Evaluation block (to be filled by evaluate.py)
        "evaluation": None,
    }
    # Also store as_of_et equal to the exact analysis time in ET (requested behavior)
    enriched["as_of_et"] = enriched["created_at_et"]

    with path.open("w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)

    # Update latest symlink
    try:
        latest = pair_dir / "latest.json"
        if latest.exists() or latest.is_symlink():
            latest.unlink()
        latest.symlink_to(path.name)
    except Exception:
        # Symlinks may not be supported on some filesystems; ignore
        pass

    return QueryRecord(path=path, timestamp=ts_readable)


__all__ = ["save_query_result", "QueryRecord", "PROVIDER_DIRS"]
