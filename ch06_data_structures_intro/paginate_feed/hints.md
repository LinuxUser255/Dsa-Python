# Hints: Paginate a Feed

## Hint 1: work out the index first

Forget code. With `page_size = 3`:

| page | index of first post | index after last post |
|------|---------------------|-----------------------|
| 1    | 0                   | 3                     |
| 2    | ?                   | ?                     |
| 3    | ?                   | ?                     |

What formula turns `page` and `page_size` into the first index? (Remember: pages start at 1, indexes start at 0.)

## Hint 2: let the list do the jumping

Once you have a start and an end index, which list feature grabs everything between them in one step,
without a loop?

## Hint 3: what happens past the end?

Try this in a REPL: `["a", "b", "c"][2:5]` and `["a", "b", "c"][10:13]`.
Does slicing past the end crash? Do you need an `if` for "page past the end"?

## Hint 4: the invalid pages

Now plug `page = -1, page_size = 3` into your formula from Hint 1. With the 10-post feed, try the
slice you get in a REPL (something like `posts[-6:-3]`).
Negative indexes don't crash. They count from the **end** of the list, so you get real posts back
when the test expects `[]`. That's why `page <= 0` needs its own check, done *before* you slice.

## Self-check

- Page 1 is missing `post1`, or every page is shifted by one? Re-check Hint 1's formula.
- Page 0 returns posts instead of `[]`? Re-read Hint 4.
- The huge-feed case fails on time? You're looping. Slices don't need a loop.
