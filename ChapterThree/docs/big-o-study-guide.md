# Big O Notation Study Guide

**Big O Notation Study Guide Based on the exercises on Boot.Dev**

<br>

## Quick Reference Table

| Big O | Name | Example | Growth |
|-------|------|---------|--------|
| O(1) | Constant | Dictionary lookup | Flat |
| O(log n) | Logarithmic | Binary search | Very slow |
| O(n) | Linear | Single loop | Steady |
| O(n log n) | Linearithmic | Merge sort | Moderate |
| O(nm) | Two variables | Nested loops (different inputs) | Depends |
| O(n²) | Quadratic | Nested loops (same input) | Fast |
| O(2ⁿ) | Exponential | Recursive fibonacci | Explosive |

---

## O(1) — Constant Time

**Definition:** Runtime doesn't change regardless of input size.

**Pattern:** Direct access, no loops over input.

```python
# Dictionary lookup is O(1)
def find_last_name(names_dict, first_name):
    return names_dict.get(first_name)
```

**Recognize it when:**
- Accessing array by index
- Dictionary/hashmap lookup
- Simple arithmetic operations
- No iteration over input

---

## O(log n) — Logarithmic Time

**Definition:** Runtime grows by one step each time input doubles.

**Pattern:** Divide and conquer — halving the problem each iteration.

```python
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False
```

**Growth example:**
| n | steps |
|---|-------|
| 8 | 3 |
| 64 | 6 |
| 1024 | 10 |
| 1048576 | 20 |

**Recognize it when:**
- Input is halved each iteration
- Binary search
- Balanced tree operations

---

## O(n) — Linear Time

**Definition:** Runtime grows proportionally with input size.

**Pattern:** Single loop through input.

```python
def find_max(nums):
    if not nums:
        return None
    
    max_value = nums[0]
    
    for num in nums[1:]:
        if num > max_value:
            max_value = num
    
    return max_value
```

**Growth example:**
| n | time |
|---|------|
| 10 | 2 ms |
| 100 | 20 ms |
| 1000 | 200 ms |

**Recognize it when:**
- Single for loop over input
- Processing each element once

---

## O(nm) — Two Variable Complexity

**Definition:** Two independent inputs affect runtime.

**Pattern:** Nested loops over different inputs.

```python
def get_avg_brand_followers(all_handles, brand_name):
    total_matching = 0
    num_influencers = len(all_handles)  # n

    for handles in all_handles:         # n iterations
        for handle in handles:          # m iterations
            if brand_name in handle:
                total_matching += 1

    if num_influencers == 0:
        return 0
    return total_matching / num_influencers
```

**Key insight:** If n and m grow at the same rate, O(nm) ≈ O(n²). Track separately when they differ.

---

## O(n²) — Quadratic Time

**Definition:** Runtime grows as the square of input size.

**Pattern:** Nested loops over the same input.

```python
def does_name_exist(first_names, last_names, full_name):
    for first in first_names:       # n iterations
        for last in last_names:     # n iterations
            if first + " " + last == full_name:
                return True
    return False
```

**Growth example:**
| n | time |
|---|------|
| 10 | 1 sec |
| 100 | 100 sec |
| 1000 | 10,000 sec |

**Recognize it when:**
- Nested loops over same input
- Comparing all pairs
- Bubble sort, selection sort

---

## Constants Don't Matter

**Key rule:** Drop constants in Big O analysis.

```
O(2n)       → O(n)
O(10n²)     → O(n²)
O(2 log(2n)) → O(log n)
```

**Why?** Big O describes growth rate, not actual runtime.

```python
# Both are O(n), even though one is "twice as slow"
def print_once(names):
    for name in names:
        print(name)

def print_twice(names):
    for name in names:
        print(name)
    for name in names:
        print(name)
```

**In practice:** Constants matter for real performance. In theory (Big O), we ignore them.

---

## Practice Problems

### Problem 1: Identify the Complexity
What is the Big O?

```python
def mystery(arr):
    for i in arr:
        for j in arr:
            print(i, j)
```

<details>
<summary>Answer</summary>
O(n²) — nested loops over the same input
</details>

---

### Problem 2: Identify the Complexity
What is the Big O?

```python
def mystery(arr):
    for i in arr:
        print(i)
    for j in arr:
        print(j)
```

<details>
<summary>Answer</summary>
O(n) — two separate loops = O(n + n) = O(2n) = O(n)
</details>

---

### Problem 3: Implement find_min
Write an O(n) function that returns the minimum value in a list.

<details>
<summary>Solution</summary>

```python
def find_min(nums):
    if not nums:
        return None
    
    min_value = nums[0]
    
    for num in nums[1:]:
        if num < min_value:
            min_value = num
    
    return min_value
```
</details>

---

### Problem 4: Count occurrences in nested list
Write a function to count how many times a name appears in a list of lists.

<details>
<summary>Solution</summary>

```python
def count_names(list_of_lists, target_name):
    count = 0
    
    for inner_list in list_of_lists:
        for name in inner_list:
            if name == target_name:
                count += 1
    
    return count
```

Complexity: O(nm) where n = number of lists, m = average list length
</details>

---

### Problem 5: Reduce the complexity
This is O(n²). Can you make it O(n)?

```python
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] == arr[j]:
                return True
    return False
```

<details>
<summary>Solution</summary>

```python
def has_duplicate(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False
```

Using a set (O(1) lookup) reduces nested loop to single loop.
</details>

---

## Cheat Sheet: How to Identify Big O

1. **No loops or recursion** → O(1)
2. **Input halved each iteration** → O(log n)
3. **Single loop** → O(n)
4. **Two nested loops (same input)** → O(n²)
5. **Two nested loops (different inputs)** → O(nm)
6. **Loop that halves + processes all** → O(n log n)

---

## Common Optimizations

| From | To | Technique |
|------|----|-----------|
| O(n²) | O(n) | Use hashmap/set for lookups |
| O(n) | O(log n) | Sort first, then binary search |
| O(n) | O(1) | Precompute / cache results |

---

## Key Takeaways

1. Big O describes **growth rate**, not actual speed
2. Always **drop constants** — O(2n) = O(n)
3. Focus on the **dominant term** — O(n² + n) = O(n²)
4. **Dictionary lookups are O(1)** — use them to optimize
5. **Binary search is O(log n)** — but requires sorted input
6. **Nested loops = multiply** — O(n) × O(n) = O(n²)
7. **Sequential loops = add** — O(n) + O(n) = O(n)
