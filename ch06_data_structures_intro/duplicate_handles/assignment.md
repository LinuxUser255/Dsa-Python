# Sets: Find Duplicate Handles

A Python `set` is an **unordered collection of unique items**. Like a dict, it's built on a hash table,
but it stores only keys, no values.

| Set operation | Big-O (average) |
|---------------|-----------------|
| `x in s` | O(1) |
| `s.add(x)` | O(1) |
| `s.remove(x)` / `s.discard(x)` | O(1) |
| `set(some_list)` | O(n) |

Compare `x in some_list`, which is **O(n)**. Swapping a list for a set when you only need membership
checks is one of the easiest big speed-ups in Python.

Two catches:

- Sets have **no order**. Never rely on the order you get when looping over one.
- Items must be **hashable**, like dict keys.

## Assignment

A bug in LockedIn's sign-up form let some people register the same handle twice.
Complete `find_duplicate_handles(handles)`.

- `handles` is a list of handle strings, in sign-up order.
- Return a list of every handle that appears **more than once**, with each such handle listed **once**.
- Sort the result alphabetically (plain `sorted()` order).
- Handles are case-sensitive: `"Ana"` and `"ana"` are different.

### Example

```python
find_duplicate_handles(["x", "y", "x", "x", "y", "z"])
# ["x", "y"]
```

### The catch

The last case is a 200,000-entry sign-up log with a **1 second** limit.

- Checking each handle against every other handle is O(n²): about 20 billion comparisons.
- `handles.count(h)` for each handle is also O(n²), because `.count()` scans the whole list.

Use sets to make it **O(n)**, plus one final sort of the duplicates.
