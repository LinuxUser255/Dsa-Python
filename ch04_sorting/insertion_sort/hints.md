# Hints: Insertion Sort

## Hint 1: two loops, two jobs

- The **outer** loop picks the next card to insert. Where should it start, and why not at 0?
- The **inner** loop walks that card left. It doesn't know in advance how far it'll go.
  Is that a `for` loop or a `while` loop?

## Hint 2: the inner loop has two stop conditions

Walking left stops when either of these is true:

1. you hit the front of the list, or
2. the item to your left is already smaller than (or equal to) yours.

Write both into the `while` condition. Which one has to be checked **first** so you never
read `nums[-1]` by accident? (In Python, `nums[-1]` doesn't crash. It quietly reads the *last* item, which is worse.)

## Hint 3: swapping

You wrote a three-line swap with a `temp` variable in `bubble_sort`. That works here too.
Python also has a one-line swap using tuple unpacking. Look at the comment at the bottom of your `bubble_sort/main.py`.

## Hint 4: trace `[3, 1, 2]` by hand

| i | j (start) | list before | swaps happen? | list after |
|---|-----------|-------------|---------------|------------|
| 1 | 1         | [3, 1, 2]   | ?             | ?          |
| 2 | 2         | ?           | ?             | ?          |

## Hint 5: "in place"

Don't build a new list. Every change should be an assignment like `nums[something] = ...`.
At the end, `return nums`, the same object you were handed.

## Self-check

- Error `must sort the list *in place*`? You're returning a new list, or `None`.
- Off by one at the front? Re-check the order of the two conditions in Hint 2.
