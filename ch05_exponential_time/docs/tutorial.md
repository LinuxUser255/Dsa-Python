# Chapter 5 Tutorial: Exponential Time

> Understand why exponential time complexity is so dangerous.

## 1. The complexity ladder

From Chapter 3, here are the classes you know, fastest to slowest:

| Big-O | Name | Example from this repo |
|-------|------|------------------------|
| O(1) | constant | `order_1/`: dictionary lookup |
| O(log n) | logarithmic | `order_log_n/`: binary search |
| O(n) | linear | `find_minimum/` |
| O(n log n) | linearithmic | `merge_sort/` |
| O(n²) | quadratic | `order_n_squared/`, `bubble_sort/` |
| **O(2ⁿ)** | **exponential** | `power_set/`, naive `fibonacci/` |
| **O(n!)** | **factorial** | `permutations/` |

Everything above the bold line is **polynomial**: O(nᵏ) for some fixed `k`. Polynomial algorithms
get slower as inputs grow, but they get slower *politely*. Exponential ones don't.

## 2. Adding vs multiplying

- **Polynomial:** doubling the input multiplies the work by a *fixed* amount. For O(n²) that's ×4,
  every time.
- **Exponential:** adding just **one** to the input multiplies the work. For O(2ⁿ) that's ×2 for
  every single extra item.

| n | n² | 2ⁿ | n! |
|---|----|----|----|
| 10 | 100 | 1,024 | 3,628,800 |
| 20 | 400 | 1,048,576 | 2.4 × 10¹⁸ |
| 30 | 900 | 1.07 × 10⁹ | 2.7 × 10³² |
| 50 | 2,500 | 1.13 × 10¹⁵ | 3.0 × 10⁶⁴ |
| 100 | 10,000 | 1.27 × 10³⁰ | 9.3 × 10¹⁵⁷ |

At a billion operations per second, 2¹⁰⁰ steps takes about **40 trillion years**, roughly 3,000 times
the age of the universe. A computer 1,000× faster only lets you handle about n = 110 instead of
n = 100. **You can't buy your way out of exponential time with better hardware.**

Run `examples/growth_table.py` to print this table with real time estimates.

## 3. Where exponential time comes from

Exponential algorithms almost always come from one of these patterns:

### a) "Try every combination"
For each of `n` items, decide **in or out**: 2ⁿ options. Examples: power set, the subset-sum problem,
picking the best combination of features.

### b) "Try every ordering"
Arrange `n` items in every order: n! options. Examples: permutations, brute-force travelling salesman.

### c) "Try every string"
Every password of length `k` from an alphabet of `c` characters: cᵏ options. See the
`exponential_growth` lesson and `examples/brute_force_pin.py`.

### d) Recursion that branches *and* repeats itself
A function that calls itself **twice** on inputs that are only slightly smaller (`n - 1` and `n - 2`)
builds a call tree that doubles at every level. If those calls overlap, it does the same work again
and again. That's the naive Fibonacci trap.

Spotting it: look for **more than one** recursive call, on inputs that **don't shrink by half**.
(Merge sort makes two calls too, but on *halves*, so it gets log n levels instead of n.)

## 4. Escaping exponential time

Sometimes you can't: if the problem asks for every subset, the *answer* is 2ⁿ long. But often the
exponential part is accidental:

### Memoization (top-down)
Cache each answer the first time you compute it, and look it up after that. If there are only `n`
*different* subproblems, the work drops from O(2ⁿ) to about O(n).
`examples/memo_call_counter.py` shows this on a grid-paths problem: millions of calls drop to a
few hundred.

### Bottom-up (tabulation)
Solve the smallest subproblems first and build upward, keeping only what you still need.
No recursion, no cache lookups.

Both are **dynamic programming**. The `fibonacci` lesson asks you to use one of them.

### Pruning, heuristics and approximation
For truly hard problems, real systems stop early when a branch can't win (*branch and bound*),
use rules of thumb (*greedy* algorithms), or accept "close enough" (*approximation algorithms*).
You'll meet the theory behind "truly hard" in **Chapter 16: P vs NP**.

## 5. When exponential is a *feature*

Cryptography depends on exponential time. A 128-bit key has 2¹²⁸ possibilities, about 3.4 × 10³⁸.
Making a password or key one unit longer multiplies an attacker's work, while barely changing yours.

## 6. Lessons in this chapter

Suggested order:

| Lesson | Function | Growth |
|--------|----------|--------|
| `exponential_growth/` | `get_num_guesses(length)` | 26ⁿ |
| `fibonacci/` | `fib(n)` | naive O(2ⁿ) → your goal O(n) |
| `power_set/` | `power_set(items)` | O(2ⁿ) |
| `permutations/` | `get_orderings(speakers)` | O(n!) |

## 7. Examples in this chapter

| File | What it shows |
|------|---------------|
| `examples/growth_table.py` | n², 2ⁿ, n! side by side with real-world time estimates |
| `examples/brute_force_pin.py` | actually cracks PINs of growing length, timing each one |
| `examples/memo_call_counter.py` | counts recursive calls before and after memoization |

```bash
python ch05_exponential_time/examples/growth_table.py
python ch05_exponential_time/examples/brute_force_pin.py
python ch05_exponential_time/examples/memo_call_counter.py
```
