# Hints: Quick Sort

## Hint 1: test `partition` on its own first

```python
>>> from main import partition
>>> nums = [9, 3, 7, 1, 5]
>>> partition(nums, 0, 4)
>>> nums
```

The pivot is `5`. Whatever order the other items end up in, what must be true about everything
left of the returned index? And about everything to its right?

## Hint 2: what `i` means

`i` points at the **last** item known to be smaller than the pivot. It starts at `low - 1`
because nothing has been found yet. Each time you find a smaller item, which do you do first:
grow the zone, or swap?

## Hint 3: trace `[9, 3, 7, 1, 5]` (pivot 5, low 0, high 4)

| j | nums[j] | < 5? | i after | list after |
|---|---------|------|---------|------------|
| 0 | 9       | ?    | -1      | ?          |
| 1 | 3       | ?    | ?       | ?          |
| 2 | 7       | ?    | ?       | ?          |
| 3 | 1       | ?    | ?       | ?          |

Then do the final pivot swap. You should end with the pivot at index 2.

## Hint 4: the `range` in `partition`

The loop must stop **before** `high`, because `high` is the pivot itself. Python's `range(a, b)` already
excludes `b`. Which `b` do you want?

## Hint 5: recursion boundaries

After partitioning, the pivot is final. Don't include it in either recursive call.
If the pivot ends at index `p`, what are the `low`/`high` pairs for the left and right sides?

## Hint 6: the base case is already written for you

`if low < high:` is the whole base case. A range of 0 or 1 items simply does nothing.
You don't need `return` statements in `quick_sort` at all.

## Self-check

- `RecursionError`? Your recursive calls probably include the pivot, so the range never shrinks.
- Mostly sorted but a few items out of place? Re-check the final swap in `partition` (`i + 1` vs `i`).
