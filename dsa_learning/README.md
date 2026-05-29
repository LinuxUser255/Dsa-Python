# DSA Learning: Real-World Crypto Analysis Examples

Learn data structures and algorithms using **real code patterns** from a production cryptocurrency analysis bot.

## 🎯 Learning Objectives

By working through these modules, you'll understand:

1. **Why** specific data structures are chosen (not just how they work)
2. **Big O complexity** in practical scenarios (not just theory)
3. **Trade-offs** when choosing algorithms
4. **Patterns** that appear in real production code

## 📚 Modules

### Module 1: Hashmaps (`01_hashmaps_db.py`)
**From:** `db.py` - Database layer for predictions

**Key Concepts:**
- O(1) lookups vs O(n) if-elif chains
- `dict.get()` for safe lookups with defaults
- Sets for O(1) membership testing
- Dict unpacking for merging

**Real-World Use:**
- Time horizon mapping (`"1h" → timedelta(hours=1)`)
- Provider routing (`"grok" → "data/queries"`)
- Config validation

**Classic Problem:** Two Sum (solved in O(n) vs O(n²))

---

### Module 2: Queues & Batch Processing (`02_queues_evaluate.py`)
**From:** `evaluate.py` - Prediction evaluation system

**Key Concepts:**
- FIFO queues with `collections.deque`
- Time-based task scheduling
- Grouping with nested dicts (`setdefault`)
- Single-pass statistics

**Real-World Use:**
- Evaluating predictions after their target time
- Grouping files by horizon and pair
- Computing accuracy statistics

**Key Insight:** `deque.popleft()` is O(1) while `list.pop(0)` is O(n)!

---

### Module 3: Caching & Validation (`03_caching_validation.py`)
**From:** `llm_client.py` - LLM API client

**Key Concepts:**
- Memoization/caching pattern
- Input validation in O(k) (constant keys)
- Probability normalization
- `argmax` to find key with max value
- Threshold-based filtering

**Real-World Use:**
- Caching API clients (avoid re-creating)
- Validating LLM probability outputs
- Edge filters for trading decisions

**Pattern:** Check cache → Return if exists → Create if not → Cache → Return

---

### Module 4: Sliding Windows (`04_sliding_windows_indicators.py`)
**From:** `market_context.py` - Technical indicator calculations

**Key Concepts:**
- Sliding window algorithms
- Single-pass vs multiple-pass
- Clustering to avoid O(n²)
- Min/max tracking in windows

**Real-World Use:**
- RSI (Relative Strength Index)
- EMA (Exponential Moving Average)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- Support/Resistance clustering

**Key Insight:** Sorting + single-pass clustering is O(n log n), much better than O(n²) pairwise comparison!

---

## 🚀 How to Use

### Run Each Module
```bash
cd dsa_learning

# Run demos and see concepts in action
python 01_hashmaps_db.py
python 02_queues_evaluate.py
python 03_caching_validation.py
python 04_sliding_windows_indicators.py
```

### Learning Path
1. **Read** the docstrings explaining concepts
2. **Run** the demos to see them in action
3. **Solve** the exercises (solutions are at the bottom!)
4. **Connect** back to the original files in `example_scripts/`

### Try the Exercises
Each module has 4 exercises. Solve them before peeking at solutions!

---

## 📊 Big O Summary

| Pattern | Complexity | Example |
|---------|------------|---------|
| Dict lookup | O(1) | `HORIZON_DELTAS.get("1h")` |
| Set membership | O(1) | `"1h" in VALID_HORIZONS` |
| List membership | O(n) | `"1h" in ["1h", "2h", ...]` |
| Dict iteration | O(n) | `for k, v in dict.items()` |
| `deque.popleft()` | O(1) | FIFO queue operations |
| `list.pop(0)` | O(n) | Shifts all elements! |
| Sorting | O(n log n) | `sorted(values)` |
| Nested loops | O(n²) | Avoid if possible! |

---

## 🔗 Connection to Real Code

| Learning Module | Real File | Key Algorithm |
|-----------------|-----------|---------------|
| `01_hashmaps_db.py` | `db.py` | O(1) horizon lookup |
| `02_queues_evaluate.py` | `evaluate.py` | FIFO task processing |
| `03_caching_validation.py` | `llm_client.py` | Client memoization |
| `04_sliding_windows_indicators.py` | `market_context.py` | RSI/MACD/Bollinger |

---

## 💡 Key Takeaways

1. **Hashmaps are everywhere** - config, caching, counting, grouping
2. **O(1) operations compound** - when called 10,000x, O(1) vs O(n) matters
3. **Choose the right data structure** - deque for queues, set for membership
4. **Avoid O(n²)** - sort + single pass beats nested loops
5. **Single-pass algorithms** - compute multiple metrics in one traversal

---

## 📖 Further Reading

- [Python Time Complexity](https://wiki.python.org/moin/TimeComplexity)
- [Real-World Algorithms](../example_scripts/real-algos-in-crypto.md)
- [Python collections module](https://docs.python.org/3/library/collections.html)
