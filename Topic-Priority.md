# Data Structures & Algorithms: Priority Learning Guide

## For CryptoAnalysisBot and Similar Projects

This document identifies which topics from the Boot.dev "Learn Data Structures and Algorithms in Python" course are most applicable to this cryptocurrency analysis bot and similar automation projects.

---

## High Relevance (Learn These First)

### 12. Hashmaps

**Why it matters:** Hashmaps (Python dictionaries) are the backbone of this project.

- `HORIZON_DELTAS` maps horizon strings to timedelta objects
- `class_probs` stores probability distributions as key-value pairs
- Market snapshots, LLM responses, and prediction records are all JSON/dict structures
- Config lookups, pair normalization, and API response parsing rely on O(1) dict access

**Practical application:** Understanding hash collisions and load factors helps you design better caching strategies for API responses and prediction storage.

---

### 3. Big-O Analysis

**Why it matters:** Evaluating algorithmic efficiency directly impacts API costs and response times.

- Batch evaluation in `evaluate.py` iterates through prediction files—understanding linear vs. logarithmic scaling matters as data grows
- API rate limits mean you need efficient algorithms that minimize external calls
- Choosing between filtering in Python vs. querying smarter affects performance

**Practical application:** When your prediction history grows to thousands of files, knowing whether your search is O(n), O(log n), or O(1) determines if reports generate in seconds or minutes.

---

### 8. Queues

**Why it matters:** The prediction evaluation system is fundamentally a queue.

- Predictions wait in a "pending" state until `target_time` passes—this is a time-based task queue
- Rate-limiting API calls (Kraken, Grok, Claude) benefits from queue-based throttling
- Batch processing workflows naturally fit FIFO patterns

**Practical application:** Implementing a proper job queue would let you schedule predictions, retries, and evaluations more elegantly than the current file-scan approach.

---

### 14. Graphs + 15. BFS and DFS

**Why it matters:** Cryptocurrency markets are interconnected networks.

- Correlation analysis between coins (how BTC movements affect ETH, altcoins) is a graph problem
- Market influence propagation can be modeled as graph traversal
- If you integrate news sentiment analysis, web crawling uses BFS/DFS patterns
- Dependency resolution (which data must be fetched before analysis) forms a DAG

**Practical application:** Building a "market influence graph" showing how price movements cascade through different coins would use these algorithms directly.

---

## Medium Relevance (Learn After Core Topics)

### 4. Sorting Algorithms

**Why it matters:** Data presentation and analysis require ordered data.

- Sorting predictions by confidence score to surface high-conviction calls
- Ranking cryptocurrencies by volatility, returns, or accuracy metrics
- Chronological ordering of historical data for charting
- Leaderboard-style reports comparing Grok vs. Claude performance

**Practical application:** Understanding stable vs. unstable sorts matters when you need secondary sort keys (e.g., sort by confidence, then by timestamp).

---

### 9. Linked Lists

**Why it matters:** Time-series data has natural sequential relationships.

- OHLC candle data forms a chain where each point connects to the next
- Sliding window calculations (moving averages, rolling volatility) traverse sequential data
- Efficient insertion/deletion when streaming real-time price updates

**Practical application:** While Python lists work fine for most cases, understanding linked structures helps when implementing streaming data pipelines or circular buffers for real-time analysis.

---

### 13. Tries

**Why it matters:** Efficient string/prefix operations for user interfaces.

- Autocomplete for cryptocurrency pair searches in the web UI
- Fast prefix matching: typing "BT" instantly suggests "BTC/USD"
- Symbol lookup optimization across multiple exchanges with different naming conventions

**Practical application:** If you expand to support hundreds of trading pairs, a trie-based autocomplete outperforms linear search through a pair list.

---

### 7. Stacks

**Why it matters:** Nested data processing and state management.

- Parsing nested JSON structures from LLM responses
- Expression evaluation if you add custom indicator formulas
- Undo/redo functionality for interactive prediction adjustments
- Call stack understanding helps debug recursive algorithms

**Practical application:** If you implement a custom formula parser for technical indicators (e.g., "SMA(20) > EMA(50)"), stack-based parsing is essential.

---

## Lower Priority (Useful for Advanced Features)

### 10. Binary Trees + 11. Red-Black Trees

**Why it matters:** Maintaining sorted data with efficient updates.

- Order book modeling (buy/sell walls) requires sorted structures with fast insertion
- Price level aggregation benefits from balanced tree properties
- Range queries ("all prices between X and Y") are efficient on BSTs

**Practical application:** If you extend into trading signals or order book analysis, balanced trees provide O(log n) insertions while maintaining sort order—better than re-sorting a list.

---

### 2. Math (Exponents, Logarithms, Factorials)

**Why it matters:** Foundation for understanding complexity and financial calculations.

- Logarithmic returns are standard in quantitative finance
- Compound growth calculations use exponentials
- Understanding O(log n) vs O(n) requires logarithm intuition

**Practical application:** Already implicit in your volatility calculations, percentage moves, and technical indicator math.

---

### 5. Exponential Time + 16. P vs NP

**Why it matters:** Recognizing intractable problems saves wasted effort.

- Portfolio optimization with constraints can become NP-hard
- Combinatorial backtesting (all parameter combinations) explodes exponentially
- Knowing when to use heuristics vs. exact solutions

**Practical application:** If you implement strategy optimization, understanding why brute-force parameter search is infeasible (and when to use genetic algorithms or simulated annealing instead) comes from this knowledge.

---

## Quick Reference: Topic to Project Feature Mapping

| Topic | Project Feature |
|-------|-----------------|
| Hashmaps | Config, API responses, prediction storage |
| Big-O | Performance optimization, scaling |
| Queues | Prediction scheduling, rate limiting |
| Graphs/BFS/DFS | Correlation analysis, market networks |
| Sorting | Reports, rankings, leaderboards |
| Linked Lists | Time-series processing, sliding windows |
| Tries | Autocomplete, symbol search |
| Stacks | JSON parsing, formula evaluation |
| Binary Trees | Order books, sorted price histories |

---

## Recommended Learning Order

1. **Hashmaps** — Immediate daily use
2. **Big-O Analysis** — Framework for all optimization decisions
3. **Queues** — Directly applicable to current architecture
4. **Sorting** — Quick wins for better data presentation
5. **Graphs + BFS/DFS** — Enables advanced correlation features
6. **Tries** — Web UI enhancements
7. **Linked Lists + Stacks** — Deeper understanding of data flow
8. **Trees** — Future trading/order book features

---

*Document generated for CryptoAnalysisBot project — applicable to similar bots including NewsAggregator, trading bots, and automation projects.*
