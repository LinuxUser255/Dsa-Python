# Hints: Power Set

## Hint 1: the base case is `[[]]`, not `[]`

`[]` means "there are no subsets". `[[]]` means "there is exactly one subset: the empty one".
How many subsets does an empty list have? (2⁰ = ?)

If you return `[]` here, every larger answer also ends up empty. Try it and see why.

## Hint 2: split the list

How do you get the first item of a list? How do you get "everything except the first item"?
You used slices like this in merge sort.

## Hint 3: trust the recursion

Assume `power_set(rest)` already works. For `["python", "sql", "go"]`, it hands you the 4 subsets
of `["sql", "go"]`. You need 8. Where do the other 4 come from?

## Hint 4: adding an item without breaking the originals

For each subset `s` from the recursive call, you need a *new* list that is `s` plus the first item.
`s.append(first)` changes `s` itself, which also changes the "without" copy you still need.
What's a way to build a **new** list instead? (Think `+`.)

## Hint 5: trace by hand

| call | rest | power_set(rest) | answer |
|------|------|-----------------|--------|
| `power_set(["sql"])` | `[]` | `[[]]` | ? |
| `power_set(["python", "sql"])` | `["sql"]` | (row above) | ? |

## Hint 6: another way, with binary counting

Number the subsets from `0` to `2ⁿ - 1`. Write each number in binary with `n` digits: each digit says
whether one item is in (1) or out (0). For `n = 2`: `00, 01, 10, 11`, which is 4 subsets.
That's a non-recursive way to do it, if you want a second challenge.

## Self-check

- Only `[[]]` comes back for every input? You're probably dropping the "without" half.
- Subsets contain duplicates of the first item? You mutated a list with `.append` (see Hint 4).
- Count is right but some subsets repeat? The "with" and "without" groups must each be built from the
  recursive result exactly once.
