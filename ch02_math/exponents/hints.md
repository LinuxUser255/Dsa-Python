# Hints: `get_estimated_spread`

> `how_to_solve.md` in this folder contains full solutions.
> If you want to solve it yourself first, use only these hints and come back to that file afterwards.

## Hint 1: two different numbers come from the same list

`[2, 3, 2, 19]` gives you two different facts:

- **how many** followers the author has
- **how big** those followers' audiences are, all added up

Which built-in gives you each one? (An earlier attempt mixed these two up; double-check which is which.)

## Hint 2: the order of the steps matters

Which step can crash if the list is empty? Make sure the guard runs **before** that step, not after.

## Hint 3: an average is always `total / count`

Say out loud which of your two numbers from Hint 1 is the total and which is the count.
If you divide them the other way round, `[12, 12, 12]` will give you something tiny instead of 12.

## Hint 4: sanity-check with the smallest test

`[100]`: one follower who has 100 followers.

- What's the average?
- What's `1 ** 1.2`?
- So what must the answer be? (The test expects `100`.)

## Hint 5: don't round it yourself

The test calls `round()` on your result. Return the raw number from the formula.

## Self-check

Run `python main_test.py` here, or `pytest ch02_math/exponents` from the repo root.
