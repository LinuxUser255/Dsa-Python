# Selection Sort

**Selection sort** is the most "obvious" sorting algorithm. Find the smallest item and put it first.
Then find the smallest of what's left and put it second. Repeat.

```
[64, 25, 12, 22, 11]
 ^ smallest of all is 11, swap it into index 0
[11, 25, 12, 22, 64]
     ^ smallest of the rest is 12, swap it into index 1
[11, 12, 25, 22, 64]
         ^ smallest of the rest is 22, swap it into index 2
[11, 12, 22, 25, 64]
             ^ 25 is already the smallest of the rest
[11, 12, 22, 25, 64]
```

## Assignment

Complete `selection_sort(nums)` in `main.py`.

1. Loop `i` over every index of `nums`. Index `i` is the spot you're about to fill.
2. Assume the smallest remaining item is at `i`. Store that **index** in `smallest_idx`.
3. Loop `j` over every index **after** `i`. If `nums[j]` is smaller than `nums[smallest_idx]`, update `smallest_idx = j`.
4. Swap `nums[i]` and `nums[smallest_idx]`.
5. Return `nums`.

As with insertion sort, **sort in place** and return the same list. The test checks this.

## Complexity

| Case    | Time  |
|---------|-------|
| Best    | O(n²) |
| Average | O(n²) |
| Worst   | O(n²) |
| Space   | O(1)  |

Notice the best case. Even a list that's already sorted still costs O(n²), because step 3 always scans
the whole remaining list. It has no early exit like bubble sort's `swapping` flag or insertion sort's
`while`.

So why learn it? Selection sort does **at most n − 1 swaps**, fewer than any other algorithm in this
chapter. When *writing* data is much more expensive than *reading* it (for example, flash memory that
wears out), that matters.
