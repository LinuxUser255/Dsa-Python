# ChapterOne/Simple_Algorithm/main.py

```python
"""
ChapterOne/Simple_Algorithm/main.py

### Goal
Create a function that takes a list of integers (`nums`) and
returns the sum of all elements. It must handle:

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

-  Once your summed(nums) correctly adds up the numbers
-  using a loop and accumulator, every test will pass.

-  `input1` and all lists get passed to `summed(nums):` function here
-  the list  [7, 4, 3, 100, 2343243, 343434, 1, 2, 32] get passed into it
"""

def summed(nums):
    total = 0
    for number in nums:
        total += number

    return total
```

<br>

# List Comprehension 

list comprehension could be used in this example to simplify the code and make it more efficient. 
List comprehension provides a concise way to create lists based on existing lists.

Here's how you could rewrite the `summed()` function using list comprehension:

```python
def summed(nums):
    return sum(num for num in nums)
```

In this version of the function, the `sum()` function is used with a generator expression that iterates over each number in the `nums` list. The `sum()` function adds up all the numbers in the list and returns the total.

List comprehension is a more concise and efficient way to achieve the same result as the original code. It can make the code easier to read and write, especially for simple operations like this one. However, it's important to note that list comprehension can sometimes make the code harder to understand, especially for more complex operations. In this case, it's a good fit because the operation is straightforward and simple.

<br>










