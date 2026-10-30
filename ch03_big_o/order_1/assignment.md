# Big-O Analysis

## Order 1 – Constant Time (O(1))

**O(1)** means that **no matter how large the input size grows**, the runtime of the algorithm remains the same.  
This is also called **constant time**.

### Classic Python Example: Dictionary Lookups

In Python, dictionaries provide extremely fast key-based lookups because the operation does **not** depend on how many items are currently stored in the dictionary.

```python
# This lookup is O(1) – constant time
org = organizations[org_id]
```

Dictionary (hash table) lookups are **O(1)** on average, which is why dictionaries (and their equivalents in other languages: HashMap, object property access, etc.) are used everywhere in performant code.

### Assignment: Fix the Slow User Search

**Problem**  
Our LockedIn user search bar is painfully slow. Users are complaining about long wait times.  
If you run the current code, you’ll notice it takes a very long time to complete searches — especially as the number of users grows.

**Goal**  
Rewrite the `find_last_name` function so that it runs in **O(1)** time — constant time — no matter how many users are in the system.

**Function Signature**

```python
def find_last_name(names_dict: dict[str, str], first_name: str) -> str | None:
    """
    Given a dictionary mapping first names to last names,
    return the last name for the given first_name.
    
    If the first_name is not found in the dictionary, return None.
    
    This function should run in O(1) time.
    
    Args:
        names_dict: Dictionary where keys are first names (str) 
                    and values are last names (str)
        first_name: The first name to look up (str)
    
    Returns:
        The corresponding last name if found, otherwise None
    """
    # Your implementation here
    pass
```

### Current (Slow) Behavior
The existing implementation is likely doing something slow, such as:

- Looping through every key in the dictionary (`for name in names_dict:`)
- Or using `.values()`, `.items()`, or other linear-time operations

Any approach that touches every entry will be **O(n)** — and will become painfully slow as the number of users grows.

### Your Task
Rewrite the function using the correct dictionary operation so that:

- It returns the last name **immediately** when the first name exists as a key
- It returns `None` when the first name is not found
- The entire operation is **O(1)** on average

### Hints

- You already know how to do constant-time lookups in Python dictionaries
- Think about the most idiomatic (and fastest) way to check if a key exists and get its value
- Avoid loops, list comprehensions, or any operation that scales with the size of `names_dict`

### Expected Time Complexity

| Operation                  | Desired Complexity | Why it matters                     |
|----------------------------|--------------------|-------------------------------------|
| Key lookup                 | **O(1)**           | Must be fast even with 1M+ users   |
| Key not found              | **O(1)**           | Same rule applies                  |
| Current (bad) linear scan  | **O(n)**           | Becomes unusable at scale          |


# Solutions comparisons

## Both worked, but what's the difference?


### mine
```python
def find_last_name(names_dict, first_name):
    return names_dict.get(first_name)
```

### boot.dev's
```python
def find_last_name(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError:
        return None

```
