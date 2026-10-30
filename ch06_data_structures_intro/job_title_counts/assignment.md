# Dictionaries: Count Job Titles

A Python `dict` maps **keys** to **values**. Under the hood it's a **hash map**: it runs the key through
a hash function to work out where the value lives, then jumps straight there. (You build one yourself
in Chapter 12: see `ch12_hashmaps/`.)

| Dict operation | Big-O (average) |
|----------------|-----------------|
| `d[key]`, `d[key] = value` | O(1) |
| `key in d` | O(1) |
| `d.get(key, default)` | O(1) |
| `del d[key]` | O(1) |
| loop over `d` / `d.items()` | O(n) |

Keys must be **hashable**: strings, numbers and tuples work; lists and dicts don't.

The most common dict pattern in real code is **counting**: one pass over the data, one dict entry per
distinct thing, and a counter that goes up.

## Assignment

LockedIn's recruiting dashboard shows how many users hold each job title.
Complete `count_job_titles(users)`.

- `users` is a list of `(name, job_title)` tuples.
- Return a dict mapping each job title to the number of users with that title.
- Titles are **case-sensitive**: `"engineer"` and `"Engineer"` are different titles.
- An empty list returns an empty dict.

### Example

```python
count_job_titles([("ana", "Engineer"), ("ben", "Designer"), ("cy", "Engineer")])
# {"Engineer": 2, "Designer": 1}
```

Your solution should make **one pass** over `users`: **O(n)**.

Python's `collections.Counter` does exactly this, and you should use it in real projects.
For this lesson, write it with a plain `dict`.
