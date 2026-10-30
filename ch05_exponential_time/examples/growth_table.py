#!/usr/bin/env python3
"""
Polynomial vs exponential vs factorial growth, with real-world time estimates.

Assumes a (generous) computer that does one billion simple steps per second.
"""

import math

STEPS_PER_SECOND = 1_000_000_000
AGE_OF_UNIVERSE_YEARS = 13.8e9


def human_time(steps):
    seconds = steps / STEPS_PER_SECOND
    units = [
        ("years", 365.25 * 24 * 3600),
        ("days", 24 * 3600),
        ("hours", 3600),
        ("minutes", 60),
        ("seconds", 1),
    ]
    if seconds < 1:
        return "instant"
    for name, size in units:
        if seconds >= size:
            amount = seconds / size
            if name == "years" and amount > AGE_OF_UNIVERSE_YEARS:
                multiple = amount / AGE_OF_UNIVERSE_YEARS
                if multiple < 1_000_000:
                    return f"{multiple:,.0f}x age of universe"
                return f"{multiple:.1e}x age of universe"
            return f"{amount:,.1f} {name}"
    return "instant"


def main():
    print(f"{'n':>4} | {'n^2':>8} | {'2^n':>26} | {'n!':>26}")
    print("-" * 72)
    for n in (5, 10, 20, 30, 40, 50, 60, 100):
        print(f"{n:>4} | {human_time(n ** 2):>8} | {human_time(2 ** n):>26} | {human_time(math.factorial(n)):>26}")

    print("\nHow big an input can each algorithm handle in ONE MINUTE?")
    budget = STEPS_PER_SECOND * 60
    print(f"  O(n^2): n = {math.isqrt(budget):,}")
    print(f"  O(2^n): n = {int(math.log2(budget))}")
    n = 1
    while math.factorial(n + 1) <= budget:
        n += 1
    print(f"  O(n!):  n = {n}")

    print("\n...and with a computer 1,000x faster?")
    budget *= 1_000
    print(f"  O(n^2): n = {math.isqrt(budget):,}   (about 32x bigger)")
    print(f"  O(2^n): n = {int(math.log2(budget))}   (only about 10 more!)")


if __name__ == "__main__":
    main()
