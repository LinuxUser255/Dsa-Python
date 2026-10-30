# Hints: Exponential Growth

## Hint 1: break it into "exactly k letters"

How many passwords have **exactly** 1 letter? Exactly 2? Exactly 3?
Write the first three out on paper. What's the pattern?

## Hint 2: which lengths are included?

"From 1 up to and including `length`." Which `range(...)` produces 1, 2, ..., `length`?
(Chapter 3's off-by-one bugs live here.)

## Hint 3: you've written this loop before

This is the running-total pattern from `simple_algorithm` (`summed`) in Chapter 1.
The only difference is *what* you add each time around the loop.

## Hint 4: the `0` case

If you build the loop correctly, does `length = 0` need its own `if`?
What does a `for` loop do over an empty range?

## Hint 5: exponent operator

Chapter 2 used `**` for exponents. `^` in Python is something else entirely (bitwise XOR):
`26 ^ 2` is `24`, not `676`.

## Self-check

- Got `676` for length 2? You only counted exactly-2-letter passwords, not lengths 1 through 2.
- Got `703` for length 2? Your range starts at `0`, so 26⁰ = 1 sneaked into the total.
- Got `18,278` for length 2? Your range goes one length too far.
