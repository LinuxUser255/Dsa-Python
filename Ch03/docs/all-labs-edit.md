# All Labs – Big O Notation

## L2: O(n) – Order “n”

**O(n)** is very common.  
When the number of steps in an algorithm grows at the same rate as its input size, it is classified as **O(n)**.

### Example: Find Minimum
The classic `find_min` algorithm is **O(n)**:

- Set `min` to positive infinity.
- For each number in the list, compare it to `min`. If smaller, update `min`.
- After the loop, `min` holds the smallest number.

The input is a list of size **n**. Because we visit each element exactly once, the runtime grows linearly.

### Runtime Scaling Example
| Input size       | Estimated time |
|------------------|----------------|
| 10 items         | 2 ms           |
| 100 items        | 20 ms          |
| 1,000 items      | 200 ms         |
| 10,000 items     | 2,000 ms       |

### Assignment
LockedIn users want to know which of their followers has the highest engagement score.

Complete the `find_max` function.  
It should take a list of integers and return the largest value.  
The runtime complexity must be **O(n)**.

**Solution**
```python
def find_max(nums):
    """Take a list of integers and return the maximum value"""
    if not nums:                    # Check if list is empty
        return None

    max_value = nums[0]             # Initialize with first element

    for num in nums[1:]:            # Loop over remaining elements
        if num > max_value:
            max_value = num

    return max_value
```

## L3: O(n²) – Order “N Squared”

**O(n²)** grows much more rapidly than **O(n)**.  
Still useful for small-to-medium inputs, but becomes problematic quickly.

A common cause of **O(n²)** is **nested loops** where both loops run over the full input size.

### Example
```python
for person_one in persons:
    for person_two in persons:
        go_on_date(person_one, person_two)
```

### Assignment
LockedIn needs (a very slow) name search for learning purposes.

Complete the `does_name_exist` function:

- For each first name in `first_names`
- For each last name in `last_names`
- If `first + " " + last` equals `full_name`, return `True`
- If no match after all combinations, return `False`

**Observe**  
Runtime grows quadratically. If inputs are length **n**, total checks ≈ **n × n**.

Rough scaling estimate (assuming 10×10 takes 1 second):

| Input size (n × n) | Estimated time    |
|---------------------|-------------------|
| 10 × 10             | 1 second          |
| 100 × 100           | 100 seconds       |
| 1,000 × 1,000       | 10,000 seconds    |
| 10,000 × 10,000     | 1,000,000 seconds |

**Solution**
```python
def does_name_exist(first_names, last_names, full_name):
    for first in first_names:
        for last in last_names:
            try:
                if first + " " + last == full_name:
                    return True
            except Exception as e:
                print(f"An error occurred while checking the name: {e}")
    return False
```

### N² Quiz

Consider:

```python
def print_names_one(first_names):
    for first_name in first_names:
        print(first_name)

def print_names_two(first_names, last_names):
    for first_name in first_names:
        for last_name in last_names:
            print(first_name, last_name)
```

- What are the Big-O complexities of `print_names_one` and `print_names_two`?  
  → **O(n), O(n²)**

- Which finishes faster (same non-zero length inputs)?  
  → **print_names_one**

## L6: O(nm)

**O(nm)** is similar to **O(n²)** but tracks two separate dimensions.

- **n** = number of outer lists (e.g., number of influencers)
- **m** = average length of inner lists (e.g., average followers per influencer)

If **n** and **m** grow at similar rates → behaves like **O(n²)**.  
Tracking separately is useful when dimensions scale differently.

### Assignment
LockedIn wants to measure brand loyalty among followers.

Complete `get_avg_brand_followers`:

- `all_handles`: list of lists of strings (handles per influencer)
- `brand_name`: string to search for
- Return: average number of handles containing `brand_name` per influencer

**Example**
```python
all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]
brand_name = "cosmo"
# → 1.33  (4 matching handles / 3 influencers)
```

**Solution**
```python
def get_avg_brand_followers(all_handles, brand_name):
    total_matching = 0
    num_influencers = len(all_handles)

    for handles in all_handles:           # n loop
        for handle in handles:            # m loop
            try:
                if brand_name in handle:
                    total_matching += 1
            except Exception as e:
                print(f"An error occurred while matching brand names to handles: {e}")
            else:
                continue

    if num_influencers == 0:
        return 0
    else:
        return total_matching / num_influencers
```

## L7: Constants Don't Matter (Part a)

Big-O describes **growth rate**, not absolute runtime.  
Constants are dropped because they do not change the asymptotic behavior.

```python
def print_names_once(names):
    for name in names:
        print(name)

def print_names_twice(names):
    for name in names: print(name)
    for name in names: print(name)
```

Both are **O(n)** — even though the second does twice as much work.

**Rule**: Drop constants  
O(2n) → **O(n)**  
O(10n²) → **O(n²)**

## L8: Constants Don't Matter (Part b)

**Question**: How would we reduce **O(2 × log(2 × n))**?

**Answer**: **O(log n)**

## L9: Constants Quiz

```python
def sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

def double_sum(nums):
    total = 0
    for num in nums:
        double = num + num
        total += double
    return total
```

**Big-O of `sum()` and `double_sum()`?**  
→ **O(n), O(n)**

## L10: Constants Quiz (Realistic Runtime)

Ignoring Big-O theory, which function takes longer in practice?  
→ **double_sum**

## L11: Order 1 – O(1)

**O(1)** = constant time — runtime does **not** grow with input size.

Classic example: dictionary key lookup

```python
org = organizations[org_id]   # O(1) average case
```

### Assignment
Fix the slow LockedIn search bar.

Complete `find_last_name` so it is **O(1)**:

```python
def find_last_name(names_dict, first_name):
    return names_dict.get(first_name)     # or names_dict[first_name] with try/except
```

## L12: Order Log N – O(log n)

**O(log n)** is only slightly slower than **O(1)** but dramatically faster than **O(n)**.

### Scaling Comparison

| n        | O(n) time | O(log n) time |
|----------|-----------|---------------|
| 8        | 8 ms      | 3 ms          |
| 64       | 64 ms     | 6 ms          |
| 1,024    | 1,024 ms  | 10 ms         |
| 1,048,576| ~1M ms    | 20 ms         |

### Binary Search – Classic O(log n) Algorithm

**Requirements**: Input list must be sorted ascending.

**Pseudocode**
- `low = 0`, `high = n-1`
- While `low <= high`:
  - `mid = (low + high) // 2`
  - If `arr[mid] == target` → return True
  - If `arr[mid] < target` → `low = mid + 1`
  - Else → `high = mid - 1`
- Return False

Each step halves the search space → logarithmic steps.

### Assignment
Implement `binary_search` (already provided in full – verify understanding):

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

## L13: Name Count – Nested Iteration

**Context**: Names often appear in nested lists (e.g., followers per influencer).

### Assignment
Complete `count_names`:

- Count total occurrences of `target_name` across all nested lists
- Observe complexity: **O(n)** total names, or **O(m × n)** where  
  m = number of lists, n = average inner list length

**Solution**
```python
def count_names(list_of_lists, target_name):
    """
    Count occurrences of target_name in nested list of lists.
    
    Time Complexity: O(total names) or O(m * n)
    Space Complexity: O(1)
    """
    count = 0
    
    for inner_list in list_of_lists:
        for name in inner_list:
            if name == target_name:
                count += 1
                
    return count
```

---

Improved formatting goals achieved:
- Consistent headings and subheadings
- Proper markdown tables
- Code blocks with language specifier
- Clear bolding of Big-O terms
- Bullet points and numbered lists where helpful
- Preserved all original content, examples, solutions, and quizzes