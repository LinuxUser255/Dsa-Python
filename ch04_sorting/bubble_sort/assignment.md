# Bubble Sort

**Bubble sort** repeatedly walks the list, comparing each pair of neighbours and swapping them if
they're out of order. After each pass, the biggest unsorted item has "bubbled up" to the end.

```
[5, 7, 3, 6, 8]
pass 1: [5, 3, 6, 7, 8]    7 bubbled past 3 and 6
pass 2: [3, 5, 6, 7, 8]    5 bubbled past 3
pass 3: no swaps, so it's sorted and we stop
```

## Assignment

LockedIn needs to sort influencers by follower count. Complete `bubble_sort(nums)`:

1. Set `swapping = True` and `end = len(nums)`.
2. While `swapping` is `True`:
   1. Set `swapping = False`.
   2. Loop `i` from `1` up to `end`. If `nums[i - 1] > nums[i]`, swap them and set `swapping = True`.
   3. Decrease `end` by one. The last item of this pass is now final, so the next pass can skip it.
3. Return `nums`.

## Complexity

See `best_worst_time_complexity.md` in this folder for the full walkthrough.

| Case    | Time  |
|---------|-------|
| Best    | O(n): already sorted, one pass with no swaps |
| Worst   | O(n²): reverse order |
| Space   | O(1): in place |
