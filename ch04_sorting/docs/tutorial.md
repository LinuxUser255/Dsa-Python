# Chapter 4 Tutorial: Sorting Algorithms

> Learn how data is sorted on a computer, and how to sort it faster.

## 1. Why sorting matters

In Chapter 3 you wrote `binary_search`, which finds an item in **O(log n)** instead of **O(n)**.
But it only works on a **sorted** list. Sorting is the price you pay up front so that every search
afterwards is cheap.

Sorting shows up everywhere on a site like LockedIn:

- feeds ordered by time
- leaderboards ordered by followers
- search results ordered by relevance
- de-duplicating data: once a list is sorted, duplicates sit right next to each other

## 2. Vocabulary

| Term | Meaning | Example |
|------|---------|---------|
| **Comparison sort** | decides order only by asking "is `a` < `b`?" | every algorithm in this chapter |
| **In place** | rearranges the original list using O(1) extra memory | bubble, insertion, selection, quick |
| **Stable** | equal items keep their original relative order | bubble, insertion, merge, Python's `sorted()` |
| **Adaptive** | runs faster when the input is already partly sorted | bubble (with the `swapping` flag), insertion |
| **Divide and conquer** | split the problem, solve the halves, combine | merge, quick |

### Why stability matters

Say you sort users by **name**, then sort that result by **job title**. With a *stable* sort, users
who share a job title stay in name order. With an unstable sort, that earlier work can be scrambled.
Run `examples/sorted_and_keys.py` to see it.

## 3. The algorithms at a glance

| Algorithm | Best | Average | Worst | Extra space | Stable | Lesson |
|-----------|------|---------|-------|-------------|--------|--------|
| Bubble    | O(n) | O(n²) | O(n²) | O(1) | yes | `bubble_sort/` |
| Merge     | O(n log n) | O(n log n) | O(n log n) | O(n) | yes | `merge_sort/` |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | yes | `insertion_sort/` |
| Quick     | O(n log n) | O(n log n) | O(n²) | O(log n) | no | `quick_sort/` |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | no | `selection_sort/` |
| Python `sorted()` | O(n) | O(n log n) | O(n log n) | O(n) | yes | `influencers/` |

Suggested order: `bubble_sort` → `merge_sort` → `insertion_sort` → `quick_sort` → `selection_sort` → `influencers`.

## 4. How big is the gap, really?

The steps below are worked out using the Big-O formulas, not timed.

| n | n log₂ n | n² |
|---|---------|----|
| 10 | 33 | 100 |
| 1,000 | ~10,000 | 1,000,000 |
| 100,000 | ~1,700,000 | 10,000,000,000 |
| 1,000,000 | ~20,000,000 | 1,000,000,000,000 |

At around 10 million simple Python steps per second, sorting 1,000,000 items takes roughly
**2 seconds** with an O(n log n) sort and roughly **a day** with an O(n²) sort.
Run `examples/count_comparisons.py` to count real comparisons yourself.

## 5. The two big ideas

### O(n²): compare everything with everything

Bubble, insertion and selection sort all have a loop inside a loop over the same list. That's the
`order_n_squared` pattern from Chapter 3. They differ only in *which* pairs they compare and *when*
they swap:

- **Bubble**: swap neighbours, repeat until a pass makes no swaps.
- **Insertion**: grow a sorted section on the left, sliding each new item into place.
- **Selection**: find the smallest remaining item, swap it into the next slot.

### O(n log n): divide and conquer

If you can split a problem in **half** and combine the halves in **O(n)**, you get
**log n levels × n work per level = O(n log n)**.

- **Merge sort** splits blindly in the middle. All the cleverness is in *combining*, the merge.
- **Quick sort** does the clever part *first*, the partition. After that, combining is free:
  the halves are already in the right places.

### Can we do better than O(n log n)?

Not with comparisons. There are `n!` possible orderings of `n` items, and each yes/no comparison can
at best cut the possibilities in half. Telling all `n!` apart takes at least `log₂(n!)` comparisons,
which works out to about `n log n`. (You'll meet `n!` again in Chapter 5.)

Non-comparison sorts like *counting sort* and *radix sort* can beat this. They don't ask `a < b`;
they use the digits or values directly. That only works for special kinds of data, like small integers.

## 6. What Python actually does

`sorted()` and `list.sort()` use **Timsort**. Since Python 3.11, its merge step follows the "Powersort" policy. Timsort:

1. scans for **runs**: stretches that are already sorted (or reverse-sorted, which it flips),
2. extends short runs with **insertion sort** (fast on small, nearly sorted pieces), then
3. **merges** runs together, like merge sort.

That's why `sorted()` is O(n) on already-sorted data, O(n log n) in the worst case, and stable. It
combines two of the algorithms you'll write in this chapter.

In real code, always use `sorted()` / `.sort()`. Write these algorithms to understand
*why* the built-in is fast, and to recognise the patterns in other problems.

## 7. `sorted()` vs `.sort()`

```python
users = ["dave", "alice", "carol"]

new_list = sorted(users)   # returns a NEW list; users is unchanged
users.sort()               # sorts users IN PLACE and returns None
```

A classic bug: `users = users.sort()`. Now `users` is `None`.

Both accept `key=` (a function that computes what to sort by) and `reverse=True`.
You'll use `key=` in the `influencers` lesson.

## 8. Examples in this chapter

| File | What it shows |
|------|---------------|
| `examples/sorted_and_keys.py` | `sorted()` vs `.sort()`, `key=`, `reverse=`, multi-key sorts, stability |
| `examples/count_comparisons.py` | counts actual comparisons made by an O(n²) sort vs Python's `sorted()` as n grows |

Run them from the repo root:

```bash
python ch04_sorting/examples/sorted_and_keys.py
python ch04_sorting/examples/count_comparisons.py
```
