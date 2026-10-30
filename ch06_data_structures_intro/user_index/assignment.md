# Choosing a Structure: Build a User Index

Data often arrives in the "wrong" shape for what you need to do with it. A list of records is great
for "go through everyone", but terrible for "find user #482,913": that's an O(n) scan **every time**.

The fix is an **index**. Pay **once**, O(n), to reorganise the data into a structure built for the
question you'll ask over and over. Then each question is **O(1)**.

This is the same trade-off as Chapter 4's "sort once, then binary search", and it's exactly what
database indexes do.

## Assignment

LockedIn's notifications service is handed a batch of user ids and needs each user's full record.
Complete both functions in `main.py`.

### `build_user_index(users)`

- `users` is a list of `(user_id, name, job_title)` tuples, in no particular order.
- Return a dict that maps each `user_id` to its **whole** tuple.

### `get_users_by_ids(index, ids)`

- `index` is the dict from `build_user_index`.
- `ids` is a list of user ids to look up.
- Return a list with one entry per id, **in the same order as `ids`**:
  the user's tuple, or `None` if no user has that id.
- The same id may be asked for more than once.

### Example

```python
users = [(7, "ana", "Engineer"), (3, "ben", "Designer"), (42, "cy", "Manager")]
index = build_user_index(users)
get_users_by_ids(index, [42, 99, 7])
# [(42, "cy", "Manager"), None, (7, "ana", "Engineer")]
```

### The catch

The last case has **300,000** users and **10,000** lookups, which must finish in **100 milliseconds**.

- Searching the user list for each id: 10,000 × 300,000 = 3 billion steps.
- Building the index once and then doing 10,000 O(1) lookups: about 310,000 steps.

User ids are **not** list positions (they go 0, 3, 6, ...), so `users[user_id]` won't work.
