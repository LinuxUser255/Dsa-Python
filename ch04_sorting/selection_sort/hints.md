# Hints: Selection Sort

## Hint 1: track an index, not a value

In Chapter 1 you wrote `find_minimum`, which tracked the smallest **value**.
Here you need to know *where* the smallest item is, so you can swap it. Which should you store?

## Hint 2: where does the inner loop start?

Everything before index `i` is already sorted and final. Should the inner loop look at those items again?
What `range(...)` gives you "every index after `i`"?

## Hint 3: trace `[3, 1, 2]`

| i | smallest_idx after inner loop | list after swap |
|---|-------------------------------|-----------------|
| 0 | ?                             | ?               |
| 1 | ?                             | ?               |
| 2 | ?                             | ?               |

## Hint 4: swapping with itself

If the smallest item is already at `i`, you swap `nums[i]` with `nums[i]`.
Is that a bug, or harmless? Do you need an `if` around the swap?

## Hint 5: the swap is in the *outer* loop

A common mistake is swapping every time a smaller item turns up, inside the inner loop.
That still sorts, but it isn't selection sort any more, and it does far more swaps.
The point of this algorithm is **one swap per position**.

## Self-check

- Error `must sort the list *in place*`? Make sure you `return nums`.
- Sorted, but count your swaps: are there more than `len(nums) - 1`? Re-read Hint 5.
