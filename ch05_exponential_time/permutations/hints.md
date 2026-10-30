# Hints: Permutations

## Hint 1: do `power_set` first

This lesson uses the same shape: base case `[[]]`, recurse on a smaller list, combine.
The difference is *how* you make the list smaller, and *how* you combine.

## Hint 2: "everyone except speaker `i`"

If you loop with an index `i`, how can you build the list without the item at `i` using two slices?
(Removing by *value* works too here, because names are unique, but don't mutate the original list.)

## Hint 3: power set vs permutations

| | power set | permutations |
|---|---|---|
| recursive call is on | everything after the **first** item | everyone except **each** item, one at a time |
| recursive calls per level | 1 | n |
| answer size | 2ⁿ | n! |

That second row is exactly where n! comes from.

## Hint 4: trace `["ana", "ben"]`

| first speaker | others | orderings of others | with first speaker in front |
|---------------|--------|---------------------|-----------------------------|
| ana           | ?      | ?                   | ?                           |
| ben           | ?      | ?                   | ?                           |

## Hint 5: building the new ordering

`[s] + ordering` creates a **new** list with `s` at the front.
`ordering.insert(0, s)` changes a list you might still need. Which one is safe here?

## Self-check

- You get `[]` back for everything? Your base case returns `[]` instead of `[[]]`.
- The count is right for 3 but not for 5? Make sure "others" removes exactly one speaker.
- Each ordering has the wrong length? You may be passing the *full* list into the recursive call.
