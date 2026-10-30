# Quick Sort

**Quick sort** is another *divide and conquer* sort, and on average it's usually the fastest
comparison sort in practice. Unlike merge sort, it sorts **in place**: no new lists.

The idea: pick one item, the **pivot**. Rearrange the list so that

- everything **smaller** than the pivot is on its left, and
- everything **bigger** is on its right.

The pivot is now in its **final** sorted position. Then quick sort the left side and the right side.

```
[9, 3, 7, 1, 5]           pivot = 5 (the last item)
[3, 1, 5, 9, 7]           partition: smaller | 5 | bigger
 ^^^^     ^^^^
quick sort [3, 1]    quick sort [9, 7]
[1, 3]               [7, 9]
[1, 3, 5, 7, 9]
```

## Assignment

Complete both functions in `main.py`. Both work on the **slice** of `nums` from index `low` to `high`,
*inclusive*. The test calls `quick_sort(nums, 0, len(nums) - 1)` and then checks `nums`.

### `partition(nums, low, high)` (the Lomuto scheme)

1. The pivot is the **last** item in the range: `nums[high]`.
2. Set `i = low - 1`. `i` marks the end of the "smaller than the pivot" zone, which starts empty.
3. Loop `j` from `low` up to (but **not** including) `high`:
   - If `nums[j]` is less than the pivot, move `i` forward one, then swap `nums[i]` and `nums[j]`.
4. Swap the pivot into place: swap `nums[i + 1]` and `nums[high]`.
5. Return `i + 1`, the pivot's final index.

### `quick_sort(nums, low, high)`

1. If `low < high` (the range has at least 2 items):
   1. Partition the range and keep the pivot's index.
   2. Quick sort the part **left** of the pivot.
   3. Quick sort the part **right** of the pivot.
2. Return nothing. The sorting happens *inside* `nums`.

## Complexity

| Case    | Time       | When |
|---------|------------|------|
| Best    | O(n log n) | each pivot lands near the middle |
| Average | O(n log n) | |
| Worst   | O(n²)      | each pivot is the smallest or largest item, e.g. an already-sorted list with a last-item pivot |
| Space   | O(log n) average | the recursion stack |

Think about that worst case. With a last-item pivot, an **already sorted** list is the worst possible input.
Real implementations avoid this by choosing the pivot randomly, or by taking the "median of three"
(first, middle, last). Merge sort never has a bad case, which is one reason Python's built-in sort is
built on merging instead.
