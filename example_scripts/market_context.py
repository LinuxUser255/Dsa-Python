from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from statistics import mean, stdev
from typing import Any, Dict, Iterable, List, Tuple, Optional
import math

from .kraken_client import fetch_ohlc_week, fetch_ticker, fetch_ohlc_since


@dataclass
class Candle:
    timestamp: int  # epoch seconds
    open: float
    high: float
    low: float
    close: float
    vwap: float
    volume: float
    count: int


def _to_candles(raw: List[Dict[str, Any]]) -> List[Candle]:
    return [
        Candle(
            timestamp=int(c["timestamp"]),
            open=float(c["open"]),
            high=float(c["high"]),
            low=float(c["low"]),
            close=float(c["close"]),
            vwap=float(c["vwap"]),
            volume=float(c["volume"]),
            count=int(c["count"]),
        )
        for c in raw
    ]


def _select_window(candles: List[Candle], start_ts: int, end_ts: int) -> List[Candle]:
    return [c for c in candles if start_ts <= c.timestamp <= end_ts]


def _find_price_at_or_before(candles: List[Candle], target_ts: int) -> float:
    candidates = [c for c in candles if c.timestamp <= target_ts]
    if not candidates:
        # Fallback to earliest close if we don't have an earlier candle
        return candles[0].close
    return candidates[-1].close


def _compute_returns(closes: Iterable[float]) -> List[float]:
    closes_list = list(closes)
    returns: List[float] = []
    for prev, curr in zip(closes_list, closes_list[1:]):
        if prev == 0:
            continue
        returns.append((curr / prev) - 1.0)
    return returns


# Valid time horizons for predictions
VALID_HORIZONS = ("1h", "2h", "4h", "6h", "12h", "24h")


def _calculate_rsi(closes: List[float], period: int = 14) -> float:
    """Calculate Relative Strength Index (RSI).
    
    RSI ranges from 0-100:
    - RSI > 70: Overbought (potential sell signal)
    - RSI < 30: Oversold (potential buy signal)
    - RSI ~50: Neutral
    
    Args:
        closes: List of closing prices (chronological order)
        period: RSI period (default: 14)
    
    Returns:
        RSI value (0-100), or 50.0 if insufficient data
    """
    if len(closes) < period + 1:
        return 50.0  # Neutral default
    
    # Calculate price changes
    deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    
    # Separate gains and losses
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    
    # Calculate average gain/loss over period
    avg_gain = mean(gains[-period:]) if len(gains) >= period else 0
    avg_loss = mean(losses[-period:]) if len(losses) >= period else 0
    
    # Avoid division by zero
    if avg_loss == 0:
        return 100.0 if avg_gain > 0 else 50.0
    
    rs = avg_gain / avg_loss
    rsi = 100.0 - (100.0 / (1.0 + rs))
    
    return rsi


def _calculate_ema(values: List[float], period: int) -> float:
    """Calculate Exponential Moving Average.
    
    Args:
        values: List of values (chronological order)
        period: EMA period
    
    Returns:
        EMA value, or last value if insufficient data
    """
    if len(values) < period:
        return values[-1] if values else 0.0
    
    multiplier = 2.0 / (period + 1)
    ema = mean(values[:period])  # Start with SMA
    
    for value in values[period:]:
        ema = (value * multiplier) + (ema * (1 - multiplier))
    
    return ema


def _calculate_macd(
    closes: List[float], fast: int = 12, slow: int = 26, signal: int = 9
) -> Tuple[float, float, float]:
    """Calculate MACD (Moving Average Convergence Divergence).
    
    Phase 2B: Fixed with proper historical MACD values for signal line.
    
    Args:
        closes: List of closing prices (chronological order)
        fast: Fast EMA period (default: 12)
        slow: Slow EMA period (default: 26)
        signal: Signal line EMA period (default: 9)
    
    Returns:
        Tuple of (macd_line, signal_line, histogram)
        - macd_line: fast_ema - slow_ema
        - signal_line: 9-period EMA of MACD line
        - histogram: macd_line - signal_line (bullish when positive)
    """
    min_periods = slow + signal
    if len(closes) < min_periods:
        return (0.0, 0.0, 0.0)  # Insufficient data
    
    # Calculate historical MACD values to compute proper signal line
    macd_values: List[float] = []
    
    for i in range(slow, len(closes) + 1):
        window = closes[:i]
        fast_ema = _calculate_ema(window, fast)
        slow_ema = _calculate_ema(window, slow)
        macd_values.append(fast_ema - slow_ema)
    
    # Current MACD line is the last value
    macd_line = macd_values[-1]
    
    # Signal line: 9-period EMA of historical MACD values
    if len(macd_values) >= signal:
        signal_line = _calculate_ema(macd_values, signal)
    else:
        signal_line = macd_line
    
    # Histogram: MACD line minus signal line
    histogram = macd_line - signal_line
    
    return (macd_line, signal_line, histogram)


def _calculate_atr(candles: List[Candle], period: int = 14) -> float:
    """Calculate Average True Range (ATR).
    
    ATR measures volatility using high/low/close.
    Higher ATR = higher volatility.
    
    Args:
        candles: List of Candle objects
        period: ATR period (default: 14)
    
    Returns:
        ATR value, or 0.0 if insufficient data
    """
    if len(candles) < period + 1:
        return 0.0
    
    true_ranges = []
    for i in range(1, len(candles)):
        high = candles[i].high
        low = candles[i].low
        prev_close = candles[i - 1].close
        
        # True range is max of:
        # 1. Current high - current low
        # 2. |Current high - previous close|
        # 3. |Current low - previous close|
        tr = max(
            high - low,
            abs(high - prev_close),
            abs(low - prev_close),
        )
        true_ranges.append(tr)
    
    # ATR is average of true ranges
    atr = mean(true_ranges[-period:]) if len(true_ranges) >= period else 0.0
    
    return atr


def _analyze_volume(
    candles: List[Candle], candles_24h: List[Candle]
) -> Dict[str, Any]:
    """Analyze volume patterns.
    
    Args:
        candles: All candles (7 days)
        candles_24h: Last 24h candles
    
    Returns:
        Dict with volume_ratio, volume_trend, volume_surge
    """
    if not candles or not candles_24h:
        return {
            "volume_ratio": 1.0,
            "volume_trend": "neutral",
            "volume_surge": False,
        }
    
    # Average volume over full period
    avg_volume_all = mean(c.volume for c in candles)
    
    # Recent 24h volume
    volume_24h = sum(c.volume for c in candles_24h)
    avg_volume_24h = volume_24h / len(candles_24h) if candles_24h else 0
    
    # Volume ratio: recent vs average
    volume_ratio = avg_volume_24h / avg_volume_all if avg_volume_all > 0 else 1.0
    
    # Volume trend: compare first half vs second half of 24h period
    if len(candles_24h) >= 12:
        mid = len(candles_24h) // 2
        vol_first_half = mean(c.volume for c in candles_24h[:mid])
        vol_second_half = mean(c.volume for c in candles_24h[mid:])
        
        if vol_second_half > vol_first_half * 1.2:
            volume_trend = "increasing"
        elif vol_second_half < vol_first_half * 0.8:
            volume_trend = "decreasing"
        else:
            volume_trend = "stable"
    else:
        volume_trend = "neutral"
    
    # Volume surge: recent volume significantly above average
    volume_surge = volume_ratio > 1.5
    
    return {
        "volume_ratio": volume_ratio,
        "volume_trend": volume_trend,
        "volume_surge": volume_surge,
    }


def _calculate_bollinger_bands(
    closes: List[float], period: int = 20, std_dev: float = 2.0
) -> Dict[str, float]:
    """Calculate Bollinger Bands (Phase 2B).
    
    Bollinger Bands measure price volatility and identify overbought/oversold conditions.
    
    Args:
        closes: List of closing prices (chronological order)
        period: SMA period (default: 20)
        std_dev: Number of standard deviations (default: 2.0)
    
    Returns:
        Dict with:
        - upper: Upper band (SMA + std_dev * σ)
        - middle: Middle band (SMA)
        - lower: Lower band (SMA - std_dev * σ)
        - bandwidth: (upper - lower) / middle * 100 (volatility measure)
        - percent_b: (price - lower) / (upper - lower) (position within bands)
    """
    if len(closes) < period:
        price = closes[-1] if closes else 0
        return {
            "upper": price,
            "middle": price,
            "lower": price,
            "bandwidth": 0.0,
            "percent_b": 0.5,
        }
    
    recent = closes[-period:]
    middle = mean(recent)
    std = stdev(recent) if len(recent) >= 2 else 0
    
    upper = middle + (std_dev * std)
    lower = middle - (std_dev * std)
    
    bandwidth = ((upper - lower) / middle * 100) if middle > 0 else 0
    current_price = closes[-1]
    percent_b = (current_price - lower) / (upper - lower) if upper != lower else 0.5
    
    return {
        "upper": upper,
        "middle": middle,
        "lower": lower,
        "bandwidth": bandwidth,
        "percent_b": percent_b,
    }


def _calculate_stochastic(
    candles: List[Candle], k_period: int = 14, d_period: int = 3
) -> Dict[str, Any]:
    """Calculate Stochastic Oscillator (Phase 2B).
    
    Stochastic measures momentum by comparing closing price to price range.
    
    Formula:
        %K = (Current Close - Lowest Low) / (Highest High - Lowest Low) * 100
        %D = SMA of %K over d_period
    
    Args:
        candles: List of Candle objects
        k_period: %K lookback period (default: 14)
        d_period: %D smoothing period (default: 3)
    
    Returns:
        Dict with:
        - k: Fast stochastic (0-100)
        - d: Slow stochastic/signal line (0-100)
        - signal: "overbought" (>80) | "oversold" (<20) | "neutral"
    """
    if len(candles) < k_period:
        return {"k": 50.0, "d": 50.0, "signal": "neutral"}
    
    # Calculate %K values for last d_period candles to compute %D
    k_values: List[float] = []
    
    for end_idx in range(len(candles) - d_period, len(candles) + 1):
        if end_idx < k_period:
            continue
        
        start_idx = end_idx - k_period
        window = candles[start_idx:end_idx]
        
        lowest_low = min(c.low for c in window)
        highest_high = max(c.high for c in window)
        current_close = window[-1].close
        
        if highest_high == lowest_low:
            k = 50.0
        else:
            k = ((current_close - lowest_low) / (highest_high - lowest_low)) * 100
        k_values.append(k)
    
    stoch_k = k_values[-1] if k_values else 50.0
    stoch_d = mean(k_values[-d_period:]) if len(k_values) >= d_period else stoch_k
    
    # Interpret signal
    if stoch_k > 80:
        signal = "overbought"
    elif stoch_k < 20:
        signal = "oversold"
    else:
        signal = "neutral"
    
    return {"k": stoch_k, "d": stoch_d, "signal": signal}


def _find_support_resistance(
    candles: List[Candle], lookback: int = 48
) -> Dict[str, Any]:
    """Identify key support and resistance levels (Phase 2B).
    
    Uses local pivot points (swing highs/lows) to find significant price levels.
    
    Args:
        candles: Price candles
        lookback: Hours to analyze (default: 48)
    
    Returns:
        Dict with:
        - support: List of support levels (below current price)
        - resistance: List of resistance levels (above current price)
        - nearest_support: Closest support level
        - nearest_resistance: Closest resistance level
    """
    if len(candles) < 3:
        price = candles[-1].close if candles else 0
        return {
            "support": [],
            "resistance": [],
            "nearest_support": price * 0.98,
            "nearest_resistance": price * 1.02,
        }
    
    recent = candles[-min(lookback, len(candles)):]
    current_price = recent[-1].close
    
    # Find local pivots (swing highs and lows)
    pivots: List[float] = []
    
    for i in range(1, len(recent) - 1):
        # Local high: higher than neighbors
        if recent[i].high > recent[i - 1].high and recent[i].high > recent[i + 1].high:
            pivots.append(recent[i].high)
        # Local low: lower than neighbors
        if recent[i].low < recent[i - 1].low and recent[i].low < recent[i + 1].low:
            pivots.append(recent[i].low)
    
    # Add absolute high/low from the period
    pivots.append(max(c.high for c in recent))
    pivots.append(min(c.low for c in recent))
    
    # Cluster nearby levels (within 0.5% of each other)
    pivots = sorted(set(pivots))
    threshold = current_price * 0.005  # 0.5% clustering threshold
    
    clustered: List[float] = []
    i = 0
    while i < len(pivots):
        cluster = [pivots[i]]
        j = i + 1
        while j < len(pivots) and pivots[j] - pivots[i] < threshold:
            cluster.append(pivots[j])
            j += 1
        clustered.append(mean(cluster))
        i = j
    
    # Separate into support (below price) and resistance (above price)
    support = sorted([p for p in clustered if p < current_price], reverse=True)
    resistance = sorted([p for p in clustered if p > current_price])
    
    # Default fallbacks if no levels found
    nearest_support = support[0] if support else current_price * 0.98
    nearest_resistance = resistance[0] if resistance else current_price * 1.02
    
    return {
        "support": support[:3],  # Top 3 closest
        "resistance": resistance[:3],
        "nearest_support": nearest_support,
        "nearest_resistance": nearest_resistance,
    }


def build_week_market_context(
    pair: str = "BTC/USD",
    *,
    as_of_end_ts: Optional[int] = None,
    use_ticker: bool = True,
    time_horizon: str = "24h",
) -> Dict[str, Any]:
    """
    Build a rich 1-week market context for ANY cryptocurrency pair from Kraken data.

    Args:
        pair: Trading pair (e.g., "BTC/USD", "XMR/USD", "ETH/USD").
        as_of_end_ts: If provided, build the context as of this UNIX epoch second.
            Candles strictly after this timestamp will be excluded (prevents leakage).
        use_ticker: If False (recommended for backtests when as_of_end_ts is set),
            the current price is taken from the last candle close instead of ticker.
        time_horizon: Prediction time horizon ("1h", "6h", "12h", or "24h").

    Behavior:
      * Fetches ~1 week of 1h OHLC candles from Kraken
      * Optionally anchors the window at as_of_end_ts (no future data)
      * Optionally fetches ticker snapshot when building live contexts
      * Computes indicators suitable for LLM analysis
    """
    if time_horizon not in VALID_HORIZONS:
        raise ValueError(f"Invalid time_horizon '{time_horizon}'. Must be one of {VALID_HORIZONS}")

    interval_minutes = 60

    if as_of_end_ts is None:
        raw_candles = fetch_ohlc_week(pair, interval_minutes=interval_minutes)
        if not raw_candles:
            raise RuntimeError(f"No OHLC candles returned from Kraken for {pair}")
        candles = _to_candles(raw_candles)
        end_ts = candles[-1].timestamp
    else:
        # Fetch at least the last 8 days prior to as_of to cover a full week
        since_ts = int(as_of_end_ts - 8 * 24 * 60 * 60)
        raw_candles = fetch_ohlc_since(pair, interval_minutes=interval_minutes, since_ts=since_ts)
        if not raw_candles:
            raise RuntimeError(f"No OHLC candles returned from Kraken for {pair} since {since_ts}")
        candles_all = _to_candles(raw_candles)
        # Slice strictly up to as_of_end_ts to avoid leakage
        candles = [c for c in candles_all if c.timestamp <= as_of_end_ts]
        if not candles:
            raise RuntimeError("No candles available at or before as_of_end_ts")
        end_ts = candles[-1].timestamp

    start_ts = max(candles[0].timestamp, end_ts - 7 * 24 * 60 * 60)
    # Keep only the last week window
    candles = _select_window(candles, start_ts, end_ts)

    # 24h reference
    ts_24h_ago = end_ts - 24 * 60 * 60

    # Potentially use ticker only when building live, not backtests
    if as_of_end_ts is None and use_ticker:
        ticker = fetch_ticker(pair)
        price_now = ticker.get("last_price", candles[-1].close)
    else:
        price_now = candles[-1].close

    price_24h_ago = _find_price_at_or_before(candles, ts_24h_ago)
    price_7d_ago = candles[0].close

    ret_24h_pct = ((price_now / price_24h_ago) - 1.0) * 100.0 if price_24h_ago else 0.0
    ret_7d_pct = ((price_now / price_7d_ago) - 1.0) * 100.0 if price_7d_ago else 0.0

    week_high = max(c.high for c in candles)
    week_low = min(c.low for c in candles)

    # Last 24h window for highs/lows/volume/MA
    candles_24h = _select_window(candles, ts_24h_ago, end_ts)
    if not candles_24h:
        candles_24h = candles[-24:]  # fallback: last 24 candles

    high_24h = max(c.high for c in candles_24h)
    low_24h = min(c.low for c in candles_24h)
    volume_24h = sum(c.volume for c in candles_24h)

    closes_all = [c.close for c in candles]
    closes_24h = [c.close for c in candles_24h]

    ma_short = mean(closes_24h) if closes_24h else price_now
    ma_long = mean(closes_all) if closes_all else price_now

    returns_7d = _compute_returns(closes_all)
    volatility_7d = stdev(returns_7d) if len(returns_7d) >= 2 else 0.0

    # Convert hourly volatility (fraction) to daily % estimate for convenience
    daily_vol_pct = (volatility_7d * math.sqrt(24) * 100.0) if volatility_7d else 0.0

    avg_volume_1h = mean(c.volume for c in candles) if candles else 0.0
    
    # Calculate technical indicators (Phase 2A)
    rsi_14 = _calculate_rsi(closes_all, period=14)
    macd_line, macd_signal, macd_histogram = _calculate_macd(closes_all)
    atr_14 = _calculate_atr(candles, period=14)
    atr_pct = (atr_14 / price_now * 100.0) if price_now > 0 else 0.0
    
    # Volume analysis
    volume_analysis = _analyze_volume(candles, candles_24h)
    
    # Phase 2B: Additional technical indicators
    bollinger = _calculate_bollinger_bands(closes_all, period=20, std_dev=2.0)
    stochastic = _calculate_stochastic(candles, k_period=14, d_period=3)
    levels = _find_support_resistance(candles, lookback=48)

    # Downsampled recent closes for the LLM (e.g. last 48 hours)
    lookback_hours_for_series = 48
    ts_lookback = end_ts - lookback_hours_for_series * 60 * 60
    candles_recent = _select_window(candles, ts_lookback, end_ts)
    recent_closes = [c.close for c in candles_recent]

    start_dt = datetime.fromtimestamp(start_ts, tz=timezone.utc)
    end_dt = datetime.fromtimestamp(end_ts, tz=timezone.utc)

    market_snapshot = {
        "current_price": price_now,
        "price_24h_ago": price_24h_ago,
        "price_7d_ago": price_7d_ago,
        "high_24h": high_24h,
        "low_24h": low_24h,
        "volume_24h": volume_24h,
    }

    indicators = {
        "ret_24h_pct": ret_24h_pct,
        "ret_7d_pct": ret_7d_pct,
        "week_high": week_high,
        "week_low": week_low,
        "ma_short": ma_short,
        "ma_long": ma_long,
        "volatility_7d": volatility_7d,
        "daily_vol_pct": daily_vol_pct,
        "avg_volume_1h": avg_volume_1h,
        "recent_closes": recent_closes,
        # Phase 2A: Advanced technical indicators
        "rsi_14": rsi_14,
        "macd": {
            "macd_line": macd_line,
            "signal_line": macd_signal,
            "histogram": macd_histogram,
        },
        "atr_14": atr_14,
        "atr_pct": atr_pct,
        "volume_ratio": volume_analysis["volume_ratio"],
        "volume_trend": volume_analysis["volume_trend"],
        "volume_surge": volume_analysis["volume_surge"],
        # Phase 2B: Bollinger Bands, Stochastic, Support/Resistance
        "bollinger": bollinger,
        "stochastic": stochastic,
        "levels": levels,
    }

    context: Dict[str, Any] = {
        "pair": pair,
        "as_of": end_dt.isoformat(),
        "time_horizon": time_horizon,
        "data_window": {
            "start": start_dt.isoformat(),
            "end": end_dt.isoformat(),
            "interval_minutes": interval_minutes,
        },
        "market_snapshot": market_snapshot,
        "indicators": indicators,
    }

    return context


# DEPRECATED: Backward compatibility wrapper
def build_btcusd_week_market_context() -> Dict[str, Any]:
    """
    DEPRECATED: Use build_week_market_context(pair="BTC/USD") instead.

    This function will be removed in version 2.0.
    """
    import warnings
    warnings.warn(
        "build_btcusd_week_market_context() is deprecated, "
        "use build_week_market_context(pair='BTC/USD')",
        DeprecationWarning,
        stacklevel=2,
    )
    return build_week_market_context("BTC/USD")


__all__ = ["build_week_market_context", "build_btcusd_week_market_context", "VALID_HORIZONS"]
