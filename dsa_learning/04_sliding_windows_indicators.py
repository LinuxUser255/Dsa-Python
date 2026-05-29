"""
DSA Learning Module: Sliding Windows and Technical Indicators
==============================================================

Real-World Application: Computing technical indicators for crypto
market analysis using sliding window algorithms.

KEY CONCEPTS:
- Sliding Window: Process contiguous subsets of data in O(n)
- Avoid O(n²): Smart algorithms that don't recompute from scratch
- Clustering: Group nearby values efficiently
- Single-pass statistics: Compute multiple metrics in one traversal
"""

from dataclasses import dataclass
from statistics import mean, stdev
from typing import Any, Dict, List, Tuple


# =============================================================================
# DATA STRUCTURE: Candle (OHLCV)
# =============================================================================

@dataclass
class Candle:
    """
    OHLCV candle - standard financial data structure.
    
    Each candle represents price action over a time interval:
    - open: Price at start of interval
    - high: Highest price during interval
    - low: Lowest price during interval
    - close: Price at end of interval
    - volume: Total traded volume
    """
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float


# =============================================================================
# CONCEPT 1: Sliding Window - RSI Calculation
# =============================================================================

def calculate_rsi(closes: List[float], period: int = 14) -> float:
    """
    Calculate Relative Strength Index using sliding window.
    
    RSI = 100 - (100 / (1 + RS))
    RS = Average Gain / Average Loss over period
    
    Time Complexity: O(n) where n = len(closes)
    - We compute price changes once: O(n)
    - We separate gains/losses: O(n)
    - We average over period: O(period) which is O(1) for fixed period
    
    The key insight: We only need the LAST `period` values!
    """
    if len(closes) < period + 1:
        return 50.0  # Neutral default
    
    # Step 1: Calculate price changes - O(n)
    deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    
    # Step 2: Separate gains and losses - O(n)
    gains = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    
    # Step 3: Average over sliding window (last `period` values) - O(period)
    avg_gain = mean(gains[-period:])
    avg_loss = mean(losses[-period:])
    
    # Avoid division by zero
    if avg_loss == 0:
        return 100.0 if avg_gain > 0 else 50.0
    
    rs = avg_gain / avg_loss
    rsi = 100.0 - (100.0 / (1.0 + rs))
    
    return rsi


# =============================================================================
# CONCEPT 2: Exponential Moving Average (EMA)
# =============================================================================

def calculate_ema(values: List[float], period: int) -> float:
    """
    Calculate Exponential Moving Average.
    
    EMA gives more weight to recent values than Simple Moving Average.
    
    Formula:
        multiplier = 2 / (period + 1)
        EMA_today = (Price_today * multiplier) + (EMA_yesterday * (1 - multiplier))
    
    Time Complexity: O(n)
    - Initialize with SMA: O(period)
    - Update through remaining values: O(n - period)
    - Total: O(n)
    
    Note: We MUST process in order - can't parallelize this!
    """
    if len(values) < period:
        return values[-1] if values else 0.0
    
    multiplier = 2.0 / (period + 1)
    
    # Initialize EMA with Simple Moving Average of first `period` values
    ema = mean(values[:period])  # O(period)
    
    # Update EMA for each subsequent value - O(n - period)
    for value in values[period:]:
        ema = (value * multiplier) + (ema * (1 - multiplier))
    
    return ema


# =============================================================================
# CONCEPT 3: MACD - Multiple EMAs Combined
# =============================================================================

def calculate_macd(
    closes: List[float],
    fast: int = 12,
    slow: int = 26,
    signal: int = 9,
) -> Tuple[float, float, float]:
    """
    Calculate MACD (Moving Average Convergence Divergence).
    
    MACD Line = Fast EMA - Slow EMA
    Signal Line = EMA of MACD Line
    Histogram = MACD Line - Signal Line
    
    Time Complexity: O(n)
    - Fast EMA: O(n)
    - Slow EMA: O(n)
    - Historical MACD values: O(n - slow)
    - Signal line: O(signal) for final EMA
    
    Total: O(n) - linear in number of price points
    """
    min_periods = slow + signal
    if len(closes) < min_periods:
        return (0.0, 0.0, 0.0)
    
    # Calculate historical MACD values to compute proper signal line
    macd_values: List[float] = []
    
    for i in range(slow, len(closes) + 1):
        window = closes[:i]
        fast_ema = calculate_ema(window, fast)
        slow_ema = calculate_ema(window, slow)
        macd_values.append(fast_ema - slow_ema)
    
    macd_line = macd_values[-1]
    signal_line = calculate_ema(macd_values, signal) if len(macd_values) >= signal else macd_line
    histogram = macd_line - signal_line
    
    return (macd_line, signal_line, histogram)


# =============================================================================
# CONCEPT 4: Stochastic Oscillator - Sliding Window with Min/Max
# =============================================================================

def calculate_stochastic(
    candles: List[Candle],
    k_period: int = 14,
    d_period: int = 3,
) -> Dict[str, float]:
    """
    Calculate Stochastic Oscillator using sliding windows.
    
    %K = (Current Close - Lowest Low) / (Highest High - Lowest Low) * 100
    %D = SMA of %K over d_period
    
    Time Complexity: O(n * k_period)
    - For each window position: O(k_period) to find min/max
    - n-k_period+1 windows total
    
    This could be optimized to O(n) using a monotonic deque for min/max,
    but the simple approach is clearer for learning.
    """
    if len(candles) < k_period:
        return {"k": 50.0, "d": 50.0, "signal": "neutral"}
    
    k_values: List[float] = []
    
    # Sliding window - compute %K for last d_period positions
    for end_idx in range(len(candles) - d_period, len(candles) + 1):
        if end_idx < k_period:
            continue
        
        start_idx = end_idx - k_period
        window = candles[start_idx:end_idx]  # O(1) slice reference
        
        # Find min/max in window - O(k_period)
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
    signal = "overbought" if stoch_k > 80 else "oversold" if stoch_k < 20 else "neutral"
    
    return {"k": stoch_k, "d": stoch_d, "signal": signal}


# =============================================================================
# CONCEPT 5: Clustering Nearby Values - O(n log n)
# =============================================================================

def cluster_levels(values: List[float], threshold_pct: float = 0.5) -> List[float]:
    """
    Cluster nearby price levels (support/resistance).
    
    Algorithm:
    1. Sort values: O(n log n)
    2. Group values within threshold: O(n) single pass
    3. Average each cluster: O(n) total
    
    Total: O(n log n) due to sorting
    
    Why this matters:
    - Raw support/resistance might have 91000, 91050, 91100
    - These are essentially the same level at ~91050
    - Clustering groups them into a single meaningful level
    
    This avoids O(n²) pairwise comparisons!
    """
    if not values:
        return []
    
    # Step 1: Sort - O(n log n)
    # Using sorted() creates a new list, preserving original
    sorted_vals = sorted(set(values))  # set() removes exact duplicates
    
    if not sorted_vals:
        return []
    
    # Calculate threshold based on first value (could use current price)
    reference = sorted_vals[len(sorted_vals) // 2]  # Median as reference
    threshold = reference * (threshold_pct / 100)
    
    # Step 2: Single-pass clustering - O(n)
    clustered: List[float] = []
    i = 0
    
    while i < len(sorted_vals):
        # Start a new cluster
        cluster = [sorted_vals[i]]
        j = i + 1
        
        # Expand cluster while values are within threshold
        while j < len(sorted_vals) and sorted_vals[j] - sorted_vals[i] < threshold:
            cluster.append(sorted_vals[j])
            j += 1
        
        # Average the cluster - O(cluster_size), but total across all is O(n)
        clustered.append(mean(cluster))
        i = j  # Move to next unprocessed value
    
    return clustered


# =============================================================================
# CONCEPT 6: Bollinger Bands - Window Statistics
# =============================================================================

def calculate_bollinger_bands(
    closes: List[float],
    period: int = 20,
    num_std: float = 2.0,
) -> Dict[str, float]:
    """
    Calculate Bollinger Bands using window statistics.
    
    Middle Band = SMA(period)
    Upper Band = Middle + (num_std * σ)
    Lower Band = Middle - (num_std * σ)
    
    Time Complexity: O(period) for the final window
    - mean(): O(period)
    - stdev(): O(period)
    
    Bandwidth and %B are derived metrics - O(1) arithmetic.
    """
    if len(closes) < period:
        price = closes[-1] if closes else 0
        return {"upper": price, "middle": price, "lower": price, 
                "bandwidth": 0.0, "percent_b": 0.5}
    
    # Use only the last `period` values (the window)
    window = closes[-period:]
    
    middle = mean(window)  # O(period)
    std = stdev(window) if len(window) >= 2 else 0  # O(period)
    
    upper = middle + (num_std * std)
    lower = middle - (num_std * std)
    
    # Derived metrics - O(1)
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


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1_simple_moving_average(values: List[float], period: int) -> float:
    """
    EXERCISE 1: Calculate Simple Moving Average of last `period` values.
    
    Given values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], period = 3
    Return: mean([8, 9, 10]) = 9.0
    
    Time complexity should be O(period), not O(n).
    """
    # YOUR CODE HERE
    pass


def exercise_2_max_in_sliding_window(values: List[int], k: int) -> List[int]:
    """
    EXERCISE 2: Find maximum in each sliding window of size k.
    
    Given values = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    
    Windows:  [1,3,-1] [3,-1,-3] [-1,-3,5] [-3,5,3] [5,3,6] [3,6,7]
    Maximums:    3        3         5         5        6       7
    
    Return: [3, 3, 5, 5, 6, 7]
    
    Simple approach: O(n*k) - find max in each window
    Optimal approach: O(n) using monotonic deque (bonus challenge!)
    """
    # YOUR CODE HERE
    pass


def exercise_3_price_changes(prices: List[float]) -> Tuple[List[float], List[float]]:
    """
    EXERCISE 3: Compute price changes and separate gains/losses.
    
    Given prices = [100, 102, 99, 101, 98]
    Changes = [2, -3, 2, -3]  # price[i] - price[i-1]
    Gains = [2, 0, 2, 0]      # positive changes, else 0
    Losses = [0, 3, 0, 3]     # absolute value of negative changes, else 0
    
    Return: (gains, losses)
    
    Do this in a single pass: O(n)
    """
    # YOUR CODE HERE
    pass


def exercise_4_find_support_resistance(
    candles: List[Candle],
    current_price: float,
) -> Tuple[List[float], List[float]]:
    """
    EXERCISE 4: Find support (below price) and resistance (above price) levels.
    
    Given a list of candles and current price:
    1. Extract all high and low values
    2. Separate into support (< current_price) and resistance (> current_price)
    3. Sort support descending (nearest first), resistance ascending (nearest first)
    
    Return: (support_levels, resistance_levels)
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# SOLUTIONS
# =============================================================================

def _solution_1(values, period):
    if len(values) < period:
        return mean(values) if values else 0.0
    return mean(values[-period:])


def _solution_2(values, k):
    if not values or k <= 0:
        return []
    result = []
    for i in range(len(values) - k + 1):
        window = values[i:i + k]
        result.append(max(window))
    return result


def _solution_3(prices):
    gains = []
    losses = []
    for i in range(1, len(prices)):
        change = prices[i] - prices[i - 1]
        gains.append(change if change > 0 else 0)
        losses.append(abs(change) if change < 0 else 0)
    return (gains, losses)


def _solution_4(candles, current_price):
    levels = []
    for c in candles:
        levels.append(c.high)
        levels.append(c.low)
    
    support = sorted([p for p in levels if p < current_price], reverse=True)
    resistance = sorted([p for p in levels if p > current_price])
    
    return (support, resistance)


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("DSA Learning: Sliding Windows & Technical Indicators")
    print("=" * 60)
    
    # Sample price data (simulated)
    closes = [
        95000, 95200, 95100, 95400, 95300,
        95600, 95500, 95800, 95700, 96000,
        95900, 96200, 96100, 96400, 96300,
        96600, 96500, 96800, 96700, 97000,
    ]
    
    # Demo 1: RSI
    print("\n1. RSI (Sliding Window on Gains/Losses):")
    rsi = calculate_rsi(closes, period=14)
    print(f"   RSI-14: {rsi:.1f}")
    print(f"   Interpretation: {'Overbought' if rsi > 70 else 'Oversold' if rsi < 30 else 'Neutral'}")
    
    # Demo 2: EMA
    print("\n2. EMA (Weighted Moving Average):")
    ema_fast = calculate_ema(closes, period=12)
    ema_slow = calculate_ema(closes, period=26)
    print(f"   EMA-12: ${ema_fast:,.0f}")
    print(f"   EMA-26: ${ema_slow:,.0f}")
    print(f"   Trend: {'Bullish' if ema_fast > ema_slow else 'Bearish'}")
    
    # Demo 3: MACD
    print("\n3. MACD (Multiple EMAs):")
    macd_line, signal_line, histogram = calculate_macd(closes)
    print(f"   MACD Line: {macd_line:.2f}")
    print(f"   Signal Line: {signal_line:.2f}")
    print(f"   Histogram: {histogram:.2f}")
    
    # Demo 4: Bollinger Bands
    print("\n4. Bollinger Bands (Window Statistics):")
    bb = calculate_bollinger_bands(closes, period=20)
    print(f"   Upper: ${bb['upper']:,.0f}")
    print(f"   Middle: ${bb['middle']:,.0f}")
    print(f"   Lower: ${bb['lower']:,.0f}")
    print(f"   %B: {bb['percent_b']:.2f} (0=lower band, 1=upper band)")
    
    # Demo 5: Clustering
    print("\n5. Level Clustering (Avoid O(n²)):")
    raw_levels = [91000, 91050, 91100, 93000, 93020, 95000]
    clustered = cluster_levels(raw_levels, threshold_pct=0.5)
    print(f"   Raw levels: {raw_levels}")
    print(f"   Clustered: {[f'{x:,.0f}' for x in clustered]}")
    
    # Demo 6: Stochastic
    print("\n6. Stochastic (Sliding Window Min/Max):")
    candles = [
        Candle(i, c-50, c+100, c-100, c, 1000)
        for i, c in enumerate(closes)
    ]
    stoch = calculate_stochastic(candles)
    print(f"   %K: {stoch['k']:.1f}")
    print(f"   %D: {stoch['d']:.1f}")
    print(f"   Signal: {stoch['signal']}")
    
    print("\n" + "=" * 60)
    print("Try the exercises!")
    print("=" * 60)
