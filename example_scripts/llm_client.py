"""Multi-provider LLM client for cryptocurrency market analysis.

Supports multiple LLM providers via the OpenAI SDK:
- Grok (xAI): Primary model for real-time predictions
- OpenAI GPT-4o: Market advisor chat, portfolio reasoning
- OpenAI GPT-4o-mini: Signal ranking, batch analysis

Usage:
    from src.llm_client import analyze_market
    
    # Default (Grok)
    result = analyze_market(market_context)
    
    # OpenAI GPT-4o (chat, reasoning)
    result = analyze_market(market_context, provider="openai")
    
    # OpenAI GPT-4o-mini (batch, cost-efficient)
    result = analyze_market(market_context, provider="openai-mini")
"""

from __future__ import annotations

import json
import logging
import os
import re
from typing import Any, Dict, List

from dotenv import load_dotenv
from openai import (
    OpenAI,
    RateLimitError,
    APIConnectionError,
    APITimeoutError,
    APIStatusError,
)
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log,
)


load_dotenv()

logger = logging.getLogger(__name__)

# =============================================================================
# Provider Configuration
# =============================================================================

PROVIDERS: Dict[str, Dict[str, str]] = {
    "grok": {
        "base_url": "https://api.x.ai/v1",
        "api_key_env": "GROK_API_KEY",
        "model": "grok-4-1-fast-reasoning",
        "description": "xAI Grok 4.1 Fast - real-time predictions",
    },
    "openai": {
        "base_url": "https://api.openai.com/v1",
        "api_key_env": "OPENAI_API_KEY",
        "model": "gpt-4o",
        "description": "OpenAI GPT-4o - market advisor, reasoning",
    },
    "openai-mini": {
        "base_url": "https://api.openai.com/v1",
        "api_key_env": "OPENAI_API_KEY",
        "model": "gpt-4o-mini",
        "description": "OpenAI GPT-4o-mini - batch analysis, cost-efficient",
    },
}

DEFAULT_PROVIDER = "grok"

# Client cache per provider
_clients: Dict[str, OpenAI] = {}


def get_client(provider: str = DEFAULT_PROVIDER) -> OpenAI:
    """Get cached OpenAI-compatible client for specified provider.

    Args:
        provider: One of 'grok', 'openai', 'openai-mini'

    Returns:
        Configured OpenAI client instance

    Raises:
        ValueError: If provider is not recognized
        RuntimeError: If API key is not set for the provider
    """
    if provider not in PROVIDERS:
        raise ValueError(
            f"Unknown provider '{provider}'. "
            f"Available: {list(PROVIDERS.keys())}"
        )

    if provider not in _clients:
        cfg = PROVIDERS[provider]
        api_key = os.getenv(cfg["api_key_env"])
        if not api_key:
            raise RuntimeError(
                f"{cfg['api_key_env']} is not set in the environment/.env "
                f"(required for provider '{provider}')"
            )
        _clients[provider] = OpenAI(
            api_key=api_key,
            base_url=cfg["base_url"],
        )
        logger.debug(f"Initialized client for provider '{provider}'")

    return _clients[provider]


def get_available_providers() -> List[str]:
    """Return list of providers that have API keys configured."""
    available = []
    for name, cfg in PROVIDERS.items():
        if os.getenv(cfg["api_key_env"]):
            available.append(name)
    return available


# Map time_horizon to human-readable labels
_HORIZON_LABELS = {
    "1h": ("1-hour", "1h", "1 hour", "in 1 hour"),
    "2h": ("2-hour", "2h", "2 hours", "in 2 hours"),
    "4h": ("4-hour", "4h", "4 hours", "in 4 hours"),
    "6h": ("6-hour", "6h", "6 hours", "in 6 hours"),
    "12h": ("12-hour", "12h", "12 hours", "in 12 hours"),
    "24h": ("24-hour", "24h", "24 hours", "tomorrow"),
}


def _build_messages(market_context: Dict[str, Any]) -> List[Dict[str, str]]:
    """Build Aladdin Prime institutional chat messages for grok-beta (Grok 4.1 Fast).

    This is the 2025-grade BlackRock Aladdin Digital Assets prompt that combines
    technical analysis with institutional risk metrics (VaR, stress tests, regime).
    """
    from .aladdin.risk_packet import build_aladdin_risk_packet

    # Build the institutional risk packet
    risk_packet = build_aladdin_risk_packet(market_context)

    system_prompt = """
You are Aladdin Prime — BlackRock's $25 trillion institutional cryptocurrency risk platform in 2025.
You receive a complete institutional data packet and must respond with exactly one valid JSON object. No explanations, no markdown, no extra text.

Schema (strict):
{
  "signal": "LONG" | "SHORT" | "HOLD",
  "confidence": 0.00-1.00,
  "directional_bias": "strongly bullish" | "bullish" | "neutral" | "bearish" | "strongly bearish",
  "entry_zone": "91300-91800" or single price,
  "stop_loss": 89650.0,
  "take_profit_targets": [93500, 95200, 97500],
  "position_size_pct_equity": X.XX,
  "max_drawdown_if_wrong_pct": X.XX,
  "var_95_1d_pct": X.XX,
  "worst_stress_scenario": "FTX 2022 → -22.7%",
  "regime": "risk-on | risk-off | bitcoin dominance | alt season | stablecoin fear | eth outperformance | low vol consolidation",
  "one_line_rationale": "<90 chars, institutional tone>",
  "detailed_rationale": "<400 words max, cite ≥1 stress test and ≥1 alt-data point>",
  "llm_summary": {"bullets": ["<key observation>"]},
  "prediction_next_day": {
    "direction_bias": "up" | "down" | "sideways" | "uncertain",
    "confidence": 0.00-1.00,
    "class_probs": {"up": X.XX, "down": X.XX, "sideways": X.XX, "uncertain": X.XX},
    "expected_move_pct_range": {"low": -X.X, "high": X.X},
    "expected_behavior": "<direction + magnitude>",
    "rationale": ["<specific reasoning>"],
    "risk_factors": ["<invalidation conditions>"],
    "disclaimer": "<risk disclosure>"
  }
}

Rules:
- HOLD is default when mixed signals or low volume/funding contradiction
- Max position = 8% equity
- Penalize LONG if funding >12% annualized
- Extreme greed (>80) + high funding (>25%) = strong SHORT bias
- Institutional accumulation (netflow < -12k BTC) = LONG bias
- Always reference at least one stress test in detailed_rationale
- class_probs MUST sum to 1.0; direction_bias = argmax(class_probs)
- Map signal: LONG→up, SHORT→down, HOLD→sideways for prediction_next_day.direction_bias
- Tone: dry, data-dense, slightly pessimistic
"""

    return [
        {"role": "system", "content": system_prompt.strip()},
        {"role": "user", "content": f"```json\n{json.dumps(risk_packet, indent=2)}\n```"},
    ]


def _extract_json(content: str) -> str:
    """Extract JSON from LLM response, handling markdown code blocks.

    Handles:
    - ```json ... ``` or ``` ... ``` wrappers
    - Leading/trailing text around JSON object
    - Nested braces (finds outermost balanced braces)
    """
    content = content.strip()

    # Handle ```json ... ``` or ``` ... ```
    code_block_match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", content)
    if code_block_match:
        content = code_block_match.group(1).strip()

    # Find balanced JSON object (handles nested braces)
    start = content.find("{")
    if start == -1:
        return content

    depth = 0
    end = start
    for i, char in enumerate(content[start:], start):
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break

    return content[start:end] if end > start else content


def _validate_prediction(
    result: Dict[str, Any], market_context: Dict[str, Any]
) -> Dict[str, Any]:
    """Validate and fix common LLM output issues.

    Ensures:
    - prediction_next_day key exists (for backward compatibility)
    - class_probs contains all 4 keys and sums to 1.0
    - direction_bias matches argmax of class_probs
    - (Phase 2A) volume confirmation for directional predictions
    
    Args:
        result: LLM output dict
        market_context: Original market context with indicators
    """
    # Normalize key: "prediction" -> "prediction_next_day" for compatibility
    if "prediction" in result and "prediction_next_day" not in result:
        result["prediction_next_day"] = result.pop("prediction")

    prediction = result.get("prediction_next_day", {})
    if not prediction:
        logger.warning("No prediction_next_day in LLM response")
        return result

    class_probs = prediction.get("class_probs", {})

    # Ensure all keys exist with default 0.0
    for key in ["up", "down", "sideways", "uncertain"]:
        if key not in class_probs:
            class_probs[key] = 0.0
        # Convert strings to floats if needed
        if isinstance(class_probs[key], str):
            try:
                class_probs[key] = float(class_probs[key])
            except ValueError:
                class_probs[key] = 0.0

    # Normalize to sum to 1.0
    total = sum(class_probs.values())
    if total > 0 and abs(total - 1.0) > 0.01:
        logger.debug(f"class_probs sum={total:.3f}, normalizing to 1.0")
        class_probs = {k: v / total for k, v in class_probs.items()}
        prediction["class_probs"] = class_probs

    # Ensure direction_bias matches argmax
    if class_probs and any(v > 0 for v in class_probs.values()):
        expected_bias = max(class_probs, key=class_probs.get)
        actual_bias = prediction.get("direction_bias", "").lower()
        if actual_bias != expected_bias:
            logger.debug(f"direction_bias mismatch: '{actual_bias}' vs argmax '{expected_bias}'")
            prediction["direction_bias"] = expected_bias

    # Ensure confidence is a float
    conf = prediction.get("confidence", 0)
    if isinstance(conf, str):
        try:
            prediction["confidence"] = float(conf)
        except ValueError:
            prediction["confidence"] = 0.5
    
    # Post-process: override low-confidence directional predictions to sideways
    # Adjusted for day trading - more aggressive thresholds for 1h/2h horizons
    horizon = market_context.get("time_horizon", "24h")
    
    # Horizon-specific confidence thresholds (lower for shorter horizons)
    MIN_DIRECTIONAL_CONFIDENCE = {
        "1h": 0.45,   # Very aggressive for 1-hour trading
        "2h": 0.48,   # Slightly more conservative
        "4h": 0.52,
        "6h": 0.55,
        "12h": 0.60,
        "24h": 0.65   # Original threshold for daily
    }.get(horizon, 0.50)  # Default to 0.50 for unknown horizons
    
    direction_bias = prediction.get("direction_bias", "")
    confidence = prediction.get("confidence", 0)
    
    # Phase 2A: Volume confirmation filter
    # Extract volume_ratio from market context
    indicators = market_context.get("indicators", {})
    volume_ratio = indicators.get("volume_ratio", 1.0)
    
    # Horizon-specific volume thresholds (disabled for very short horizons)
    LOW_VOLUME_THRESHOLD = {
        "1h": 0.4,    # Very permissive for 1-hour (noise is expected)
        "2h": 0.45,
        "4h": 0.5,
        "6h": 0.6,
        "12h": 0.65,
        "24h": 0.7    # Original threshold for daily
    }.get(horizon, 0.5)
    
    override_reason = None
    
    if direction_bias in ["up", "down"]:
        # Check confidence threshold
        if confidence < MIN_DIRECTIONAL_CONFIDENCE:
            override_reason = f"insufficient confidence ({confidence:.2f})"
        # Check volume confirmation (Phase 2A)
        elif volume_ratio < LOW_VOLUME_THRESHOLD:
            override_reason = f"low volume ({volume_ratio:.2f}x avg, requires ≥{LOW_VOLUME_THRESHOLD}x)"
        
        if override_reason:
            logger.debug(f"Overriding {direction_bias} to sideways: {override_reason}")
            prediction["direction_bias"] = "sideways"
            
            # Update class_probs to reflect sideways
            if "class_probs" in prediction:
                # Transfer up/down probability to sideways
                old_prob = prediction["class_probs"].get(direction_bias, 0)
                prediction["class_probs"]["sideways"] = prediction["class_probs"].get("sideways", 0) + old_prob
                prediction["class_probs"][direction_bias] = 0
            
            # Add note to rationale
            rationale = prediction.get("rationale", [])
            if isinstance(rationale, list):
                rationale.append(f"[Auto-adjusted: {override_reason}]")
                prediction["rationale"] = rationale

    # ──────────────────────────────────────────────────────────────
    # NEW (2025 calm edge filter) — only act when we actually have edge
    # Adjusted for day trading with horizon-specific thresholds
    # ──────────────────────────────────────────────────────────────
    indicators = market_context.get("indicators", {})
    alt_data = result.get("alt_data", {})  # injected by risk_packet

    funding_ann = alt_data.get("funding_annualized_pct", 5.0)
    fg_index = alt_data.get("fear_greed_index", 50)
    regime = result.get("regime_cluster", "neutral")

    # Simple but extremely effective penalties/bonuses
    funding_penalty = max(0.0, (funding_ann - 18.0) / 100)   # >18% → heavy LONG penalty
    funding_bonus   = max(0.0, (-10.0 - funding_ann) / 100)  # <–10% → heavy SHORT penalty
    regime_bonus = 1.3 if "accumulation" in regime.lower() else 1.0

    edge = prediction.get("confidence", 0.5) * regime_bonus * (1 - funding_penalty - funding_bonus)

    prediction["edge_score"] = round(edge, 3)
    
    # Horizon-specific edge thresholds (lower for shorter horizons = more trades)
    EDGE_THRESHOLD = {
        "1h": 0.42,   # Very aggressive for hourly trading
        "2h": 0.45,
        "4h": 0.50,
        "6h": 0.55,
        "12h": 0.62,
        "24h": 0.68   # Original conservative threshold
    }.get(horizon, 0.50)
    
    if edge < EDGE_THRESHOLD:
        prediction["direction_bias"] = "sideways"
        rationale = prediction.get("rationale", [])
        if isinstance(rationale, list):
            rationale.append(f"[Edge filter: {edge:.2f} < {EDGE_THRESHOLD} → no trade]")
            prediction["rationale"] = rationale

    # CRITICAL: Cap confidence when funding is extreme (less strict for short horizons)
    # For hourly trading, allow trades even with extreme funding if confidence is high
    funding_cap = 0.45 if horizon in ["1h", "2h"] else 0.35
    
    if funding_ann > 18.0 and prediction.get("direction_bias") == "up":
        prediction["confidence"] = min(prediction.get("confidence", 0), funding_cap)
    if funding_ann < -10.0 and prediction.get("direction_bias") == "down":
        prediction["confidence"] = min(prediction.get("confidence", 0), funding_cap)

    # ──────────────────────────────────────────────────────────────

    return result


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=30),
    retry=retry_if_exception_type((
        RateLimitError,
        APIConnectionError,
        APITimeoutError,
        APIStatusError,
    )),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)
def analyze_market(
    market_context: Dict[str, Any],
    provider: str = DEFAULT_PROVIDER,
) -> Dict[str, Any]:
    """Analyze market with specified LLM provider.

    Supports multiple providers via the OpenAI SDK:
    - 'grok': xAI Grok 4.1 Fast (default) - real-time predictions
    - 'openai': OpenAI GPT-4o - market advisor, portfolio reasoning
    - 'openai-mini': OpenAI GPT-4o-mini - batch analysis, cost-efficient

    Retries up to 3 times with exponential backoff (2s, 4s, 8s...) on:
    - Rate limit errors (429)
    - Connection errors
    - Timeout errors
    - Server errors (5xx)

    Args:
        market_context: Market data dict from build_week_market_context()
        provider: LLM provider to use ('grok', 'openai', 'openai-mini')

    Returns:
        Dict with keys: llm_summary, prediction_next_day, signal, etc.
    """
    client = get_client(provider)
    model = PROVIDERS[provider]["model"]
    messages = _build_messages(market_context)

    kwargs: Dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": 0.1,   # deterministic = higher consistency on short horizons
    }

    # Seed support (Grok and OpenAI both support this)
    seed_env = os.getenv("LLM_SEED")
    if seed_env:
        try:
            kwargs["seed"] = int(seed_env)
        except ValueError:
            pass
    elif provider == "grok":
        # Default seed for Grok for reproducibility
        kwargs["seed"] = 424242

    logger.debug(f"Calling {provider} ({model}) for market analysis")
    completion = client.chat.completions.create(**kwargs)
    content = completion.choices[0].message.content.strip()

    # Force JSON-only clean output (safety layer)
    json_match = re.search(r'\{.*\}', content, re.DOTALL)
    if not json_match:
        raise ValueError(f"LLM ({provider}) failed to return valid JSON")
    json_str = json_match.group(0)

    # Extract and parse JSON (handles nested braces)
    json_str = _extract_json(json_str)

    try:
        result = json.loads(json_str)
    except json.JSONDecodeError as e:
        logger.error(f"JSON parse failed ({provider}): {e}\nRaw content: {content[:500]}")
        raise ValueError(f"LLM ({provider}) returned invalid JSON: {e}") from e

    # Add provider metadata
    result["_provider"] = provider
    result["_model"] = model

    # Validate and normalize (pass market_context for volume check)
    result = _validate_prediction(result, market_context)

    return result


# Backward compatibility alias
def analyze_market_with_grok(market_context: Dict[str, Any]) -> Dict[str, Any]:
    """Legacy alias for analyze_market(provider='grok').

    Deprecated: Use analyze_market(market_context, provider='grok') instead.
    """
    return analyze_market(market_context, provider="grok")


def analyze_market_with_openai(
    market_context: Dict[str, Any],
    model: str = "gpt-4o",
) -> Dict[str, Any]:
    """Analyze market with OpenAI GPT-4o or GPT-4o-mini.

    Args:
        market_context: Market data dict from build_week_market_context()
        model: 'gpt-4o' (default) or 'gpt-4o-mini'

    Returns:
        Dict with keys: llm_summary, prediction_next_day, signal, etc.
    """
    provider = "openai" if model == "gpt-4o" else "openai-mini"
    return analyze_market(market_context, provider=provider)


__all__ = [
    # Core functions
    "analyze_market",
    "analyze_market_with_grok",
    "analyze_market_with_openai",
    "get_client",
    "get_available_providers",
    # Constants
    "PROVIDERS",
    "DEFAULT_PROVIDER",
]
