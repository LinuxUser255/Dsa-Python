# Data Structures & Algorithms in CryptoAnalysisBot

This document demonstrates the practical applications of high-relevance data structures and algorithms throughout the CryptoAnalysisBot codebase, with a focus on hashmaps and Big O notation considerations.

## 1. **Hashmaps (Python Dictionaries) - O(1) Access**

Hashmaps are the backbone of this project, providing constant-time lookups for configuration, API responses, and prediction storage.

### Core Examples

#### Time Horizon Mapping
```python
# src/db.py:14-21
# Map time horizon strings to timedelta
HORIZON_DELTAS = {
    "1h": timedelta(hours=1),
    "2h": timedelta(hours=2),
    "4h": timedelta(hours=4),
    "6h": timedelta(hours=6),
    "12h": timedelta(hours=12),
    "24h": timedelta(hours=24),
}
```
This hashmap provides **O(1) lookup** for time horizon conversions, critical for performance when processing thousands of predictions.

#### Probability Distribution Storage
```python
# src/llm_client.py:171
"class_probs": {"up": X.XX, "down": X.XX, "sideways": X.XX, "uncertain": X.XX},
```
Probability distributions stored as hashmaps for **O(1) access** to prediction classes.

#### Efficient Key Validation
```python
# src/llm_client.py:256-267
# Ensure all keys exist with default 0.0
for key in ["up", "down", "sideways", "uncertain"]:
    if key not in class_probs:  # O(1) membership check
        class_probs[key] = 0.0
    # Convert strings to floats if needed
    if isinstance(class_probs[key], str):
        try:
            class_probs[key] = float(class_probs[key])
        except ValueError:
            class_probs[key] = 0.0
```

## 2. **Big O Analysis in Practice**

The codebase demonstrates conscious awareness of algorithmic complexity in critical paths.

### Linear O(n) Iteration vs. O(1) Dictionary Access

```python
# scripts/evaluate.py:107-121
for json_file in pair_dir.glob("*.json"):  # O(n) iteration
    # Skip symlinks (like latest.json)
    if json_file.is_symlink():
        continue
    
    try:
        with json_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Check if already evaluated - O(1) dict access
        if data.get("evaluation") is not None:
            continue
        
        # Check if target_time exists and has passed
        target_time_str = data.get("target_time")  # O(1)
        if not target_time_str:
            continue
```

### Avoiding O(n²) with Smart Data Structures

```python
# src/market_context.py:421-435
# Cluster nearby levels (within 0.5% of each other)
pivots = sorted(set(pivots))  # O(n log n) sort
threshold = current_price * 0.005  # 0.5% clustering threshold

clustered: List[float] = []
i = 0
while i < len(pivots):  # O(n) single pass instead of O(n²)
    cluster = [pivots[i]]
    j = i + 1
    while j < len(pivots) and pivots[j] - pivots[i] < threshold:
        cluster.append(pivots[j])
        j += 1
    clustered.append(mean(cluster))
    i = j
```

## 3. **Queue Patterns (Time-Based Task Queue)**

The prediction evaluation system fundamentally implements a queue pattern for deferred processing.

### Task Scheduling
```python
# src/db.py:92-95
# Calculate target evaluation time based on horizon
horizon_delta = HORIZON_DELTAS.get(time_horizon, timedelta(hours=1))  # O(1) lookup
target_dt = ts_dt + horizon_delta
target_et = target_dt.astimezone(ZoneInfo("America/New_York"))
```

### Queue Processing (FIFO)
```python
# scripts/evaluate.py:121-127
# Check if target_time exists and has passed
target_time_str = data.get("target_time")
if not target_time_str:
    continue

target_time = parse_iso_datetime(target_time_str)
if target_time <= now:  # Task becomes eligible (FIFO queue behavior)
    pending.append(json_file)
```

## 4. **Efficient Caching with Hashmaps**

Technical indicators are cached in nested dictionaries for rapid access during analysis.

```python
# src/aladdin/signal_engine.py:78-90
pair = market_context.get("pair", "BTC/USD")
indicators = market_context.get("indicators", {})
levels = indicators.get("levels", {})

# Extract indicators - all O(1) operations
rsi = indicators.get("rsi_14", 50)
macd = indicators.get("macd", {})
macd_hist = macd.get("histogram", 0)
macd_line = macd.get("macd", 0)
macd_signal = macd.get("signal", 0)
stochastic = indicators.get("stochastic", {})
stoch_k = stochastic.get("k", 50)
stoch_d = stochastic.get("d", 50)
```

## 5. **Performance-Optimized Data Access**

### Directory Hierarchy as Implicit Hashmap

The file system structure acts as a multi-level hashmap:
```
data/queries/{HORIZON}/{PAIR}/YYYY-MM-DD_HH-MM_ET.json
```
- Level 1: Horizon → O(1) directory access
- Level 2: Pair → O(1) subdirectory access
- Result: Efficient organization for thousands of predictions

### Batch Processing for O(n) Operations

```python
# scripts/accuracy_report.py:216-227
for json_file in pair_dir.glob("*.json"):  # O(n) where n = files in one pair
    if json_file.is_symlink():
        continue
    
    try:
        with json_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Skip if not evaluated - O(1) check
        evaluation = data.get("evaluation")
        if evaluation is None:
            continue
```

## 6. **Algorithm Complexity Considerations**

### Sliding Window Calculations - O(n)
```python
# src/market_context.py:343-354
k_values: List[float] = []

for end_idx in range(len(candles) - d_period, len(candles) + 1):  # O(d_period)
    if end_idx < k_period:
        continue
    
    start_idx = end_idx - k_period
    window = candles[start_idx:end_idx]  # O(1) slice reference
    
    lowest_low = min(c.low for c in window)  # O(k_period)
    highest_high = max(c.high for c in window)  # O(k_period)
    current_close = window[-1].close
```
Total complexity: O(d_period × k_period), but with small constants (14 × 3 typical).

### Normalization to Avoid Re-computation
```python
# src/llm_client.py:270-274
# Normalize to sum to 1.0
total = sum(class_probs.values())  # O(4) - constant for 4 keys
if total > 0 and abs(total - 1.0) > 0.01:
    logger.debug(f"class_probs sum={total:.3f}, normalizing to 1.0")
    class_probs = {k: v / total for k, v in class_probs.items()}  # O(4)
```

## 7. **Real-World Performance Impact**

### Provider Directory Separation
```python
# src/db.py:28-31
PROVIDER_DIRS = {
    "grok": Path("data") / "queries",         # Default (existing)
    "claude": Path("data") / "queries_claude",  # Claude A/B test
}
```
O(1) provider routing prevents linear search through mixed predictions.

### Signal Classification with Hashmaps
```python
# src/aladdin/signal_engine.py:83-90
# Extract indicators - all O(1) operations avoiding repeated computation
rsi = indicators.get("rsi_14", 50)
macd = indicators.get("macd", {})
macd_hist = macd.get("histogram", 0)
```

### Edge Calculation Optimization
```python
# src/llm_client.py:362-379
# Horizon-specific edge thresholds stored in dictionary
EDGE_THRESHOLD = {
    "1h": 0.42,   # Very aggressive for hourly trading
    "2h": 0.45,
    "4h": 0.50,
    "6h": 0.55,
    "12h": 0.62,
    "24h": 0.68   # Original conservative threshold
}.get(horizon, 0.50)  # O(1) lookup with default
```

## Key Takeaways

1. **Hashmaps dominate** the codebase for configuration (`HORIZON_DELTAS`), API responses, and prediction storage
2. **O(1) dictionary access** is leveraged everywhere instead of linear searches
3. **File system structure** acts as a hierarchical hashmap for efficient data organization
4. **Queue patterns** are implicit in the pending prediction evaluation system
5. **Big O awareness** shows in:
   - Avoiding nested loops where possible
   - Using sorted sets for deduplication
   - Batch processing to amortize I/O costs
6. The codebase demonstrates **practical algorithm optimization** for handling thousands of prediction files efficiently

## Performance Characteristics Summary

| Operation | Complexity | Location | Impact |
|-----------|------------|----------|--------|
| Horizon lookup | O(1) | `db.py:HORIZON_DELTAS` | Critical for every prediction |
| Price fetch | O(1) | API calls with caching | Reduces API load |
| File scanning | O(n) | `evaluate.py` | Scales linearly with predictions |
| Pivot clustering | O(n log n) | `market_context.py` | Efficient support/resistance |
| Indicator extraction | O(1) | `signal_engine.py` | Fast signal generation |
| Probability normalization | O(k) where k=4 | `llm_client.py` | Constant time validation |

## Practical Implications

### Scalability
- Current design handles ~10,000 predictions efficiently
- Directory structure prevents O(n²) growth
- Hashmap lookups keep response times constant

### Memory Efficiency
- Lazy loading via file system "database"
- No need to hold all predictions in memory
- O(1) access to latest prediction via symlinks

### Maintenance
- Clear separation of concerns through dictionary structures
- Easy to add new horizons or providers
- Performance characteristics remain predictable

This document demonstrates how fundamental computer science concepts directly impact real-world performance in a production cryptocurrency analysis system. The conscious use of appropriate data structures and awareness of algorithmic complexity ensures the system remains responsive even as data volume grows.