## Sorting Algorithms

### Overview
- **Why sorting matters**: Almost every modern web application depends on sorted data at some level.
  - Database lookups (e.g., finding a user profile) often use sorted indexes (B-trees, covered in later courses).
  - Leaderboards, feeds, search results, recommendation lists, and analytics dashboards all rely on ordering.
- **Built-in sorting in Python**:
  - `sorted()` function (returns new sorted list)
  - `.sort()` method (in-place sorting on lists)
  - Both are highly optimized implementations of **Timsort** — a hybrid of merge sort and insertion sort.
- **Key learning goal**:
  - Understand how to customize sorting behavior using the `key` parameter.
  - Apply a derived metric (vanity score) to control sort order.
  - Connect sorting to real-world use cases like ranking users or content.
- **Big-O reminder** (from **Big-O Analysis**):
  - Python’s `sorted()` is **O(n log n)** average and worst case.
  - Avoid worse-than-linear approaches when sorting is unnecessary.

### Assignment: Sort Influencers by Vanity Score

**Problem**  
We want to rank influencers in LockedIn by a custom “vanity” metric.  
Higher vanity = more attention-seeking behavior (more links in bio + more selfies).

**Goal**  
Implement two functions:
1. `vanity(influencer)` — computes a vanity score for one influencer
2. `vanity_sort(influencers)` — returns a new list of influencers sorted from **lowest** to **highest** vanity

**Function Signatures**

```python
def vanity(influencer):
    """
    Calculate the vanity score for a single influencer.
    
    Vanity score = (number of links in bio × 5) + number of selfies
    
    Args:
        influencer: An Influencer object with attributes:
                    - bio_links: int (number of URLs in their bio)
                    - selfies: int (number of selfie photos posted)
    
    Returns:
        int: The computed vanity score
    """
    # Your implementation here
    pass


def vanity_sort(influencers):
    """
    Return a new list of influencers sorted by increasing vanity score.
    
    Args:
        influencers: list[Influencer] — list of influencer objects
    
    Returns:
        list[Influencer]: New list sorted from lowest to highest vanity
    
    Time Complexity: O(n log n) due to sorted() / Timsort
    Space Complexity: O(n) for the new sorted list
    """
    # Your implementation here
    pass
```

### How It Works
- **Vanity score formula**:
  ```
  vanity = (bio_links × 5) + selfies
  ```
  - Links are weighted 5× more heavily than selfies (marketing value of links in bio).
- **Sorting requirement**:
  - Use Python’s `sorted()` function.
  - Pass a custom `key` function that tells `sorted()` to compare influencers based on their vanity score.
  - Default sort order is ascending (lowest to highest vanity).

**Example**  
```python
class Influencer:
    def __init__(self, name, bio_links, selfies):
        self.name = name
        self.bio_links = bio_links
        self.selfies = selfies

influencers = [
    Influencer("Ava", 2, 10),     # vanity = 2×5 + 10 = 20
    Influencer("Ben", 0, 3),      # vanity = 0×5 + 3  = 3
    Influencer("Cleo", 4, 5),     # vanity = 4×5 + 5  = 25
]

sorted_list = vanity_sort(influencers)
# Result order: Ben (3), Ava (20), Cleo (25)
```

### Hints for Solving
1. **Implement `vanity`** first — it’s simple arithmetic:
   ```python
   return influencer.bio_links * 5 + influencer.selfies
   ```
2. **For `vanity_sort`**, use `sorted()` with the `key` parameter:
   - The `key` function should take one influencer and return its vanity score.
   - Syntax: `sorted(influencers, key=vanity)`
   - Or define an inline lambda: `sorted(influencers, key=lambda inf: inf.bio_links * 5 + inf.selfies)`
3. **Do NOT** modify the original list unless explicitly asked (use `sorted()` not `.sort()`).
4. **Edge cases** to consider:
   - Empty list → return empty list
   - All influencers have same vanity score → stable sort preserves original order
   - Zero links or zero selfies
   - Very large numbers (but Python ints handle it fine)
5. **No need** for manual sorting algorithms here — leverage Python’s built-in **O(n log n)** sort.

### Learning Connections
- **Sorting Algorithms**: You’re using Timsort indirectly — understanding its hybrid nature helps explain why it’s so fast in practice.
- **Key functions**: A powerful pattern used in many Python APIs (e.g., `max()`, `min()`, `groupby`).
- **Future topics**:
  - Custom comparators → leads to understanding **Red Black Trees** and balanced BSTs (used in database indexes).
  - When built-in sort isn’t enough → implement your own (e.g., **MergeSort**, **QuickSort**).
  - Stable vs. unstable sorting → important for multi-level sorts.

Test your functions with small lists and print vanity scores to verify ordering! This is a great step toward mastering real-world data ordering and ranking logic.