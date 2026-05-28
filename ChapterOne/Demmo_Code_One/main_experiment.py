#!/usr/bin/env python3
"""
Implement the "find minimum" algorithm in Python
by completing  the find_minimum() function.
It accepts a list of integers nums and returns the smallest number
in the list.

# set current_min to a very large number like infinity
# initializes a "tracker" variable called minimum to positive infinity
"""


def find_minimum(nums):
    minimum = float('inf') # set current_min to a very large number like infinity
    if len(nums) == 0:
        return None

    for num in nums:
        # This is the core of the algorithm:
        # progressively refining the smallest
        # value found so far.
        if num < minimum:
            minimum = num
    return minimum


def main():
    find_minimum([1, 2, 3, 4, 5])
    # 1, 2, 3, 4, 5 are passed as arguments to the nums parameter in the find_minimum function


if __name__ == "__main__":
    main()
