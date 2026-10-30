# Hints: Find Duplicate Handles

## Hint 1: what do you need to remember?

Walk through `["x", "y", "x", "x"]` one handle at a time, as if you were reading a paper sign-up sheet.
When you reach the second `"x"`, how do you *know* it's a duplicate? What did you have to remember
from earlier?

## Hint 2: two collections

You need to keep track of two different things as you go:

1. every handle you've **seen** so far
2. every handle you've found to be a **duplicate**

Which data structure answers "have I seen this before?" in O(1)?

## Hint 3: why the duplicates collection should also be a set

In `["x", "x", "x"]`, the third `"x"` is a duplicate again. If your duplicates collection were a list,
what would end up in it? A set makes "list each duplicate once" automatic.

## Hint 4: the final shape

The test wants a **sorted list**. A set has no order. Which built-in turns any collection into a sorted list?

## Hint 5: a dict alternative

You could also count every handle with a dict (like `job_title_counts`), then keep the handles whose
count is above 1. That's O(n) too. Try both ways if you like.

## Self-check

- Small cases pass but the big one times out? Look for `in some_list` or `.count(` inside a loop.
- The same handle appears twice in your output? Re-read Hint 3.
- Right handles, wrong order? Don't forget to sort.
