# Hints: Merge Sort

Try one hint at a time, then go back to the code.

## Hint 1: write `merge` first, and test it on its own

`merge` doesn't depend on `merge_sort` at all. Before touching recursion, try it in a REPL:

```python
>>> from main import merge
>>> merge([1, 4, 9], [2, 3, 10])
```

What should that print? If `merge` is right, `merge_sort` is only a few lines more.

## Hint 2: tracing `merge` by hand

`first = [1, 4, 9]`, `second = [2, 3, 10]`. Fill in the table on paper:

| i | j | first[i] | second[j] | take | final so far |
|---|---|----------|-----------|------|--------------|
| 0 | 0 | 1        | 2         | ?    | ?            |
| ? | ? | ?        | ?         | ?    | ?            |

When does the loop stop? What's still left over, and in which list?

## Hint 3: the leftovers

When your `while` loop ends, one list is used up and the other may still have items.
Those leftovers are already sorted *and* all bigger than everything in `final`.
Do they need comparing, or can they just go on the end? (A slice can help.)

## Hint 4: the base case

Every recursive function needs a way to **stop**. What's the smallest list that is already sorted
with no work at all? What happens if you forget this check and call `merge_sort([7])`?

## Hint 5: splitting

You need a middle index. Given `len(nums)`, how do you get a whole-number midpoint?
(Chapter 3's `binary_search` used the same operator.) Then use slices for the two halves.

## Hint 6: putting it together

`merge_sort` should *trust itself*: assume the recursive calls hand back sorted halves.
Its only job is to split, recurse, and hand both results to `merge`.

## Self-check

- `merge_sort([])` and `merge_sort([1])` should return without recursing.
- Error `'NoneType' object is not subscriptable`? One of your functions is missing a `return`.
- Small cases pass but the 20,000 case times out? Check that you split in **half**.
  Peeling off one item at a time makes it O(n²).
