Let's break this down step by step as we think about implementing the `find_minimum` function. I'll guide you through the reasoning process for solving problems like finding the smallest value in a list of numbers. This is a classic "linear search" for a minimum—simple but foundational in algorithms. We'll focus on logic and pseudocode to build your understanding, not the final code.

### Step 1: Understand the Problem
First, always clarify what the function needs to do:
- Input: A list of integers (e.g., [7, 4, 3, 100]).
- Output: The smallest integer in that list (e.g., 3).
- Edge cases: What if the list is empty? (The instructions suggest returning None.) What if all numbers are the same? What if there's only one number?
- Goal: Scan the list once to find the minimum without sorting (sorting would be less efficient for large lists).

Think about efficiency: For a list of n elements, the best way is to check each one (O(n) time complexity), as you can't assume the list is sorted.

### Step 2: Initialize a Tracker
To find the smallest value, you need a way to keep track of the "current smallest" as you go through the list.
- Start with a value that's guaranteed to be larger than any possible number in the list. In pseudocode:
  ```
  set current_min to a very large number  # like infinity
  ```
- Why infinity? It ensures the first real number you encounter becomes the new minimum. This handles lists with negative numbers too.

If the list is empty, you can check that right away and return something special (like None) before proceeding.

### Step 3: Iterate Through the List
Now, loop over each element in the list:
- For each number, compare it to your current_min.
- If it's smaller, update current_min to that number.
- Pseudocode example:
  ```
  for each num in the list:
      if num < current_min:
          set current_min to num
  ```
- This is a simple comparison loop. Think: Why does this work? Because you're progressively narrowing down to the smallest by only updating when you find something better.

Test this mentally with a small example: List [5, 3, 8].
- Start: current_min = infinity.
- First num=5: 5 < infinity? Yes, update to 5.
- Next num=3: 3 < 5? Yes, update to 3.
- Next num=8: 8 < 3? No, stay at 3.
- End: Smallest is 3.

### Step 4: Handle the Result
After the loop:
- If the list wasn't empty, current_min now holds the smallest value—return it.
- If it was empty, you already handled it earlier.

Consider: What if the list has duplicates (e.g., [2, 2, 2])? The loop still finds 2 correctly.

### Step 5: Test Your Logic
Before writing code, mentally run more cases:
- Empty list: Return None.
- Single element: It becomes the min.
- All decreasing: Min is the last.
- All increasing: Min is the first.
- Negatives: Works since infinity handles them.

This thinking process—problem breakdown, initialization, iteration, edge cases—applies to many search problems (e.g., max, specific value). Now, try sketching your own pseudocode or walking through another example list. What questions do you have next?