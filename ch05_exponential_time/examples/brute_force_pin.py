#!/usr/bin/env python3
"""
Brute-force a numeric PIN by trying every possibility, and time it.

Each extra digit multiplies the number of guesses by 10: O(10^n).
The secret is always the WORST case (all 9s, the very last guess),
so you can watch the time column grow by about 10x per row.
"""

import itertools
import time

DIGITS = "0123456789"


def crack(secret):
    """Try every PIN of the same length until one matches. Returns the number of guesses."""
    guesses = 0
    for attempt in itertools.product(DIGITS, repeat=len(secret)):
        guesses += 1
        if "".join(attempt) == secret:
            return guesses
    return guesses


def main():
    print(f"{'digits':>6} | {'possible PINs':>14} | {'guesses needed':>14} | {'time':>10}")
    print("-" * 56)
    elapsed, guesses = 0.0, 1
    for length in range(1, 8):
        secret = "9" * length
        start = time.perf_counter()
        guesses = crack(secret)
        elapsed = time.perf_counter() - start
        print(f"{length:>6} | {10 ** length:>14,} | {guesses:>14,} | {elapsed:>9.4f}s")

    seconds_per_guess = elapsed / guesses
    print("\nEach row is about 10x the last. Extrapolating from your machine's speed:")
    for length in (10, 12, 16):
        hours = seconds_per_guess * 10 ** length / 3600
        if hours < 48:
            estimate = f"{hours:,.1f} hours"
        elif hours < 24 * 365:
            estimate = f"{hours / 24:,.1f} days"
        else:
            estimate = f"{hours / (24 * 365.25):,.1f} years"
        print(f"  {length}-digit PIN: about {estimate}")
    print("That multiplying is why longer passwords are stronger, and why exponential")
    print("algorithms are only usable for tiny inputs.")


if __name__ == "__main__":
    main()
