# Exponential Growth

An algorithm is **exponential**, O(2ⁿ) or more generally O(cⁿ), when every extra unit of input
*multiplies* the work by a constant instead of *adding* to it.

Compare with polynomial growth:

| n  | n² (polynomial) | 2ⁿ (exponential) |
|----|-----------------|------------------|
| 10 | 100             | 1,024            |
| 20 | 400             | 1,048,576        |
| 30 | 900             | 1,073,741,824    |
| 60 | 3,600           | 1,152,921,504,606,846,976 |

Going from n = 30 to n = 60 makes the n² algorithm **4×** slower and the 2ⁿ algorithm
**a billion times** slower.

The good news is that exponential growth is what keeps your passwords safe.

## Assignment

LockedIn's security team wants to show users why short passwords are dangerous. An attacker who knows
your password uses only lowercase letters `a`–`z`, and is at most `length` characters long, has to try:

- every 1-letter password,
- every 2-letter password,
- ... up to every `length`-letter password.

Complete `get_num_guesses(length)`. It returns the **total** number of passwords the attacker must try
for all lengths from `1` up to and including `length`.

- With 26 possible letters, there are `26 ** k` different passwords of exactly `k` letters.
- If `length` is `0`, there's nothing to guess: return `0`.

### Example

`get_num_guesses(2)`:

- 1-letter passwords: 26
- 2-letter passwords: 26² = 676
- total: **702**

## Things to notice once it passes

- Adding **one** character multiplies the answer by about **26**. That's exponential growth working
  *for* you.
- A 10-letter lowercase password has about 1.5 × 10¹⁴ possibilities. At a billion guesses per second,
  that's under two days. Adding uppercase letters, digits and symbols makes the base about 94 instead
  of 26, and *that* is where the strength comes from.
- `examples/brute_force_pin.py` actually cracks short PINs, so you can watch the time multiply.
