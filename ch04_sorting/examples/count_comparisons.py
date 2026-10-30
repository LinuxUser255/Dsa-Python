#!/usr/bin/env python3
"""
Count how many comparisons each sort really makes as the input grows.

Big-O is a prediction. This script measures it:
    - an O(n^2) sort (the bubble sort you already wrote)
    - Python's built-in sorted(), which is O(n log n)

Each time n doubles, watch the ratio of comparisons:
    O(n^2)     -> roughly x4
    O(n log n) -> a bit more than x2
"""

import math
import random
from functools import cmp_to_key


def bubble_sort_comparisons(nums):
    """Your bubble sort from bubble_sort/main.py, with a comparison counter added."""
    nums = list(nums)
    comparisons = 0
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            comparisons += 1
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True
        end -= 1
    return comparisons


def builtin_sort_comparisons(nums):
    """Counts the comparisons sorted() makes by routing each one through a counting function."""
    count = 0

    def compare(a, b):
        nonlocal count
        count += 1
        return (a > b) - (a < b)

    sorted(nums, key=cmp_to_key(compare))
    return count


def main():
    random.seed(1)
    print(f"{'n':>6} | {'bubble':>12} | {'sorted()':>10} | {'n^2':>12} | {'n log2 n':>10}")
    print("-" * 62)
    n = 250
    while n <= 4000:
        nums = [random.randint(0, 1_000_000) for _ in range(n)]
        print(
            f"{n:>6} | {bubble_sort_comparisons(nums):>12,} | "
            f"{builtin_sort_comparisons(nums):>10,} | {n * n:>12,} | {round(n * math.log2(n)):>10,}"
        )
        n *= 2

    already_sorted = list(range(4000))
    print("\nOn an ALREADY SORTED list of 4,000 items:")
    print(f"  bubble sort: {bubble_sort_comparisons(already_sorted):,} comparisons (best case O(n))")
    print(f"  sorted():    {builtin_sort_comparisons(already_sorted):,} comparisons (Timsort spots the sorted run)")


if __name__ == "__main__":
    main()
