# Hints: Mutual Connections

## Hint 1: which row of the table?

"Appears in **both** lists". Look at the table in `assignment.md`. Which set operation is that?

## Hint 2: lists in, set operations in the middle, list out

The operations in the table only work on sets, not lists. What do you need to do to the inputs first?
And what does the test want back: a set, or something else?

## Hint 3: duplicates for free

`["ana", "ana", "ben"]` contains `"ana"` twice. What happens to that duplicate when the list becomes a set?
Do you need any extra code for the "each handle once" rule?

## Hint 4: if you write the loop yourself

You don't *have* to use `&`. A loop over one list, checking membership in the **other**, is fine,
as long as that other one is a **set** and not a list. Why does that one change matter so much for the
100,000-user case?

## Self-check

- The large case times out? Some `x in <list>` is still inside a loop.
- `["cy", "ana"]` instead of `["ana", "cy"]`? Sets have no order: sort before you return.
