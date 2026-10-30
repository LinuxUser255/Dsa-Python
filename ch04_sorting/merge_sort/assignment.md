# Merge Sort

Bubble sort works, but it's **O(n²)**. LockedIn now has tens of thousands of influencers, and sorting
them by follower count takes far too long. We need a sort that stays fast as the list grows.

**Merge sort** is a *divide and conquer* algorithm:

1. **Divide:** split the list in half, again and again, until every piece has 0 or 1 items.
   A list with 0 or 1 items is already sorted.
2. **Conquer:** **merge** pairs of sorted pieces back together into bigger sorted pieces,
   until you have one sorted list again.

```
[5, 7, 3, 6]
      split
[5, 7]      [3, 6]
 split       split
[5] [7]     [3] [6]       <- 1 item each: already sorted
 merge       merge
[5, 7]      [3, 6]
      merge
[3, 5, 6, 7]
```

All the real work happens in **merge**. Merging two lists that are *already sorted* is easy:
look only at the front of each list, take the smaller item, and repeat.

## Assignment

Complete both functions in `main.py`.

### `merge_sort(nums)`

1. If `nums` has fewer than 2 items, return it as-is. This is the **base case** that stops the recursion.
2. Split `nums` into a first half and a second half.
3. Call `merge_sort` on each half.
4. Return the result of `merge`-ing the two sorted halves.

### `merge(first, second)`

`first` and `second` are each already sorted, smallest first. Return **one new list** that holds every item from both,
also sorted smallest first.

1. Create an empty `final` list.
2. Keep an index into `first` (`i`) and an index into `second` (`j`), both starting at 0.
3. While **both** lists still have items left:
   - If `first[i] <= second[j]`, append `first[i]` to `final` and move `i` forward.
   - Otherwise append `second[j]` and move `j` forward.
4. One list is now used up. Append whatever is left in the other list.
5. Return `final`.

Don't use `sorted()` or `.sort()`. Writing the algorithm is the point.

## Why it's fast

- Halving `n` until you hit 1 takes **log n** levels. (Remember logarithms from Chapter 2?)
- On each level, merging touches every item once: **n** work.
- Total: **O(n log n)**. For 20,000 items that's about 286,000 steps, compared with about 400,000,000 for bubble sort.

The submit cases include a 20,000-number list with a **1 second** limit. An O(n²) sort won't make it.

| Case    | Time       |
|---------|------------|
| Best    | O(n log n) |
| Average | O(n log n) |
| Worst   | O(n log n) |
| Space   | O(n): `merge` builds new lists |

Merge sort is also **stable**: equal items keep their original order, thanks to the `<=` in step 3.
