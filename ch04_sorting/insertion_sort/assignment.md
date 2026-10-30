# Insertion Sort

Merge sort is fast on big lists, but it builds lots of new lists along the way. For **small** or
**nearly sorted** lists, a simpler algorithm often wins: **insertion sort**.

It's how most people sort a hand of playing cards. Pick up one card at a time and slide it
left until it sits in the right spot among the cards you're already holding.

```
[5, 2, 4, 1]      sorted part | unsorted part
[5 | 2, 4, 1]     2 < 5, slide 2 left
[2, 5 | 4, 1]     4 < 5, slide left; 4 > 2, stop
[2, 4, 5 | 1]     1 slides all the way to the front
[1, 2, 4, 5]
```

The left part of the list is always sorted. Each step grows it by one item.

## Assignment

LockedIn's "recently active" list is *almost* sorted already: users only shift a few spots between refreshes.
Complete `insertion_sort(nums)` in `main.py`.

1. Loop `i` over every index from `1` to the end of the list. Index `0` alone is already a "sorted part".
2. Set `j = i`.
3. While `j > 0` **and** the item at `j - 1` is bigger than the item at `j`:
   - swap the items at `j - 1` and `j`
   - move `j` one step left
4. Return `nums`.

**Sort in place.** Rearrange the items inside the list you were given, then return that same list.
The test checks this, so `return sorted(nums)` won't pass.

## Complexity

| Case    | Time  | When |
|---------|-------|------|
| Best    | O(n)  | the list is already sorted: the `while` loop never runs |
| Average | O(n²) | |
| Worst   | O(n²) | the list is in reverse order: every item slides all the way left |
| Space   | O(1)  | in place |

Even though its worst case matches bubble sort, insertion sort is used in practice.
Python's own sort (Timsort) uses insertion sort on small chunks before merging them.
