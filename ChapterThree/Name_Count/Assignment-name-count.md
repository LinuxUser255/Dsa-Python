## Name Count

### Overview
- **Context**: Processing user data in LockedIn (a fictional social platform) frequently involves **nested lists** (lists of lists).
- **Real-world example**: Each outer list could represent an influencer's followers, with each inner list containing usernames.
- **Core task**: Traverse a nested list structure to count all occurrences of a specific `target_name`.
- **Learning focus**:
  - **Data Structures Intro**: Working with 2D lists / arrays
  - **Big-O Analysis**: Understanding time complexity of nested iteration
- **Key principle**: Efficient traversal should be linear in the total number of names — no unnecessary overhead.
- **Comparison**: Similar mindset to traversing **Linked Lists** sequentially or visiting nodes in **Graphs** without redundant work.

### Assignment: Implement the Name Count Function
**Problem**  
Count how many times `target_name` appears across **all** names in a nested list of lists.  
Useful for analytics tasks such as:
- Detecting duplicate usernames
- Measuring name popularity in follower groups

**Goal**  
Complete the `count_names` function so it returns the total count efficiently (no redundant operations).

**Function Signature**

```python
def count_names(list_of_lists: list[list[str]], target_name: str) -> int:
    """
    Count the occurrences of target_name in a nested list of lists.
    
    Args:
        list_of_lists: A list containing inner lists of strings (names)
        target_name: The name to count (str)
    
    Returns:
        int: The total count of target_name across all inner lists
    
    Time Complexity: O(n) where n is the total number of names
                     (or O(m * n) with m outer lists and n average inner length)
    Space Complexity: O(1) - no extra space beyond a counter
    """
    # Your implementation here
    pass
```

### How It Works
- Input is a **2D list** (list of lists of strings), e.g.:  
  `[["Alice", "Bob"], ["Alice", "Charlie"], ["Bob"]]`
- Algorithm must:
  - Visit **every** name in **every** inner list
  - Increment a counter each time `target_name` is found
  - Return the final count (returns 0 for empty structures or no matches)

**Example**  
```python
list_of_lists = [["Alice", "Bob", "Alice"], ["Charlie"]]
target_name = "Alice"
# → returns 2
```

### Time Complexity (Tying to Big-O Analysis)
- **Optimal**: **O(n)** — where n = total number of names across all lists  
  (you must examine every name at least once)
- **Alternative view**: **O(m × n)**  
  - m = number of outer lists  
  - n = average length of each inner list  
  → still linear in total elements
- **What to avoid**:
  - Sorting → **O(n log n)** (from **Sorting Algorithms**)
  - Unnecessary recursion → risk of **Exponential Time** in bad cases
- **Space**: **O(1)** — only a single integer counter is needed  
  (no **Hashmaps**, **Stacks**, **Queues**, or other structures required)

### Hints for Solving
1. Use **nested loops**:
   - Outer loop: iterate over each inner list
   - Inner loop: iterate over each name in that list
2. Initialize `count = 0` before looping
3. Inside the inner loop: `if name == target_name: count += 1`
4. Handle important **edge cases**:
   - Empty outer list: `[]`
   - Lists containing empty inner lists: `[[]]`, `[[], [], []]`
   - No matches at all
   - Target appears in every position
5. Keep it simple — no need for advanced structures like **Queues**, **BFS/DFS**, or **Binary Trees**
6. Optional concise style (for learning, not required):
   ```python
   return sum(1 for sublist in list_of_lists for name in sublist if name == target_name)
   ```
   → but explicit loops are clearer when first learning iteration

This exercise strengthens your ability to work with nested data — a foundation for later topics like **Tries** (prefix-based name search), **Graphs** (user connection networks), and **Hashmaps** (fast lookups by name).  
Test with small examples to build confidence!

## My solution vs Boot.Dev's
```python
def count_names(list_of_lists, target_name):
    """
    Core task: Traverse a nested list structure to count all occurrences of a specific `target_name`

        Count how many times `target_name` appears across all names in a nested list of lists.

        Args:
            `list_of_lists`: A list containing inner lists of strings (names)
            `target_name`: The name to count (str)

        Returns:
            int: The total count of `target_name` across all inner lists

        Time Complexity: O(n) where n is the total number of names
                         (or O(m * n) with m outer lists and n average inner length)

                         n = number of lists
                         m = average length of each list

        Space Complexity: O(1) - no extra space beyond a counter
        """
    # Step 1. Initialize a counter for the target name
    count = 0

    # Step 2. Iterate over each inner list
    for inner_list in list_of_lists:

        # Step 3. Iterate over each name in the inner list
        for name in inner_list:

            # Step 4. If the current name matches the target, increment the counter
            if name == target_name:
                count += 1

    return count

```

## Boot.Dev's
```python
def count_names(list_of_lists, target_name):
    count = 0
    for inner_list in list_of_lists:
        for name in inner_list:
            if target_name == name:
                count += 1
    return count

```

### Same code, mine just has more comments and doc strings