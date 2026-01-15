#!/usr/bin/env python3

"""
Sure, let's walk through the implementation logic for `summed(nums)` one more
time—clear, step-by-step, using the tests as our guide.

### Goal
Create a function that takes a list of integers (`nums`) and returns the sum of
all elements. It must handle:

- Normal lists with positives
- Empty list (`[]` → 0)
- Single element
- Negative numbers
- Large numbers
- Lists of zeros

### Core Logic Breakdown

1. **Initialize an accumulator**
   Start with a variable that will hold the running total. Set it to `0`.
   Why 0? It's the additive identity—adding 0 to any number doesn't change it.
   This automatically handles the empty list case (nothing added → total stays 0).

2. **Iterate through the list**
   Loop over each number in `nums`. A simple `for` loop works perfectly since
   addition is order-independent.

3. **Add each number to the accumulator**
   Inside the loop, add the current number to the running total.

4. **Return the final total**
   After the loop finishes, the accumulator contains the full sum—return it.

### Mental Simulation with Test Cases
- `[]`: total starts at 0, loop runs 0 times → return 0 ✓
- `[1]`: total = 0 + 1 → return 1 ✓
- `[-1, -2, -3]`: 0 + (-1) = -1 → -1 + (-2) = -3 → -3 + (-3) = -6 ✓
- `[12, 12, 12]`: 0 + 12 + 12 + 12 → 36 ✓
- Large mixed list: adds everything correctly → 2686826 ✓

### Key Insights
- No extra data structures needed—just one variable.
- Time complexity: O(n) — we touch each element once.
- Space complexity: O(1) — constant extra space.
- This is a classic "reduction" or "accumulation" pattern—very common in algorithms.

You're building a solid foundation. Once you implement this simple loop, all 8
tests in `main_test.py` should pass. Ready to try writing it yourself now? Let me know how it goes! 😊
"""

def summed(nums):
    """
    1. **Initialize an accumulator**
       Start with a variable that will hold the running total. Set it to `0`.

    2. **Iterate through the list**
       Loop over each number in `nums`. A simple `for` loop works perfectly since
       addition is order-independent.
    """
    nums = [0] # start with an empty list

    for number in nums:
        print(number)


def main():
    """Entry point."""
    summed(nums=[1, 2, 3, 4, 5])


if __name__ == "__main__":
    main()

