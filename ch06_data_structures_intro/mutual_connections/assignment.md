# Set Operations: Mutual Connections

Sets come with the operations from maths class built in:

| Operation | Operator | Method | Result |
|-----------|----------|--------|--------|
| union        | `a \| b` | `a.union(b)` | in **either** set |
| intersection | `a & b` | `a.intersection(b)` | in **both** sets |
| difference   | `a - b` | `a.difference(b)` | in `a` but **not** `b` |
| symmetric difference | `a ^ b` | `a.symmetric_difference(b)` | in exactly **one** of them |

An intersection costs about **O(min(len(a), len(b)))**, because Python loops over the smaller set and
does an O(1) lookup in the bigger one. Building each set from a list is O(n).

## Assignment

When you visit someone's LockedIn profile, it shows "**N mutual connections**".
Complete `get_mutual_connections(connections_a, connections_b)`.

- Each argument is a list of handles, one user's connections.
- Return a list of every handle that appears in **both** lists.
- Each handle appears **once** in the result, even if a list repeats it.
- Sort the result alphabetically.

### Example

```python
get_mutual_connections(["ana", "ben", "cy"], ["cy", "dee", "ana"])
# ["ana", "cy"]
```

### The catch

The last case compares two networks of **100,000** users each, with a 1 second limit.

- `for handle in connections_a: if handle in connections_b` is O(n × m), about 10 billion steps,
  because `in` on a **list** is O(n).
- With sets, the whole thing is **O(n + m)** plus a final sort.
