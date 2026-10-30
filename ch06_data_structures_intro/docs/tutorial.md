# Chapter 6 Tutorial: Data Structures Intro

> Learn about data structures and how they play a critical role in algorithms.

## 1. What is a data structure?

A **data structure** is a way of **organising data in memory** so that certain operations are cheap.

Every structure is a trade-off. None of them is fast at *everything*. Choosing one means asking:

> *"What will I do with this data **most often**?"*

Then pick the structure that makes *that* operation fast.

You've already seen this in action:

- `order_1/` (Chapter 3) went from O(n) to O(1) just by using a dict instead of looping.
- `binary_search` (Chapter 3) only works because the data is kept **sorted**.
- `ch12_hashmaps/` is where you build a dict yourself, from scratch.

**Algorithms and data structures come as a pair.** The right structure often makes the algorithm trivial.

## 2. Python's four built-in workhorses

| | `list` | `tuple` | `dict` | `set` |
|---|---|---|---|---|
| Literal | `[1, 2]` | `(1, 2)` | `{"a": 1}` | `{1, 2}` |
| Ordered? | yes | yes | insertion order (3.7+) | **no** |
| Mutable? | yes | **no** | yes | yes |
| Duplicates? | yes | yes | keys unique | **no** |
| Look up by | position | position | key | membership |
| Under the hood | dynamic array | fixed array | hash table | hash table |

Note: `{}` is an empty **dict**. An empty set is `set()`.

## 3. The Big-O cheat sheet

| Operation | list | dict | set |
|-----------|------|------|-----|
| get by index / key | O(1) | O(1)* | n/a |
| `x in ...` | **O(n)** | O(1)* | O(1)* |
| add to end / add key | O(1)† | O(1)* | O(1)* |
| insert / remove at front | **O(n)** | n/a | n/a |
| remove by value / key | O(n) | O(1)* | O(1)* |
| loop over all items | O(n) | O(n) | O(n) |
| sort | O(n log n) | n/a | n/a |

\* *average* case. Hash tables can degrade with many collisions; you'll see why in Chapter 12.
† *amortised*: usually O(1), occasionally the array has to grow and copy.

**The single most useful row is `x in ...`.** `x in some_list` inside a loop is the most common
accidental O(n²) in Python. Run `examples/membership_timing.py` to see the gap.

## 4. How they work (the short version)

### Arrays: `list` and `tuple`

Items sit **side by side** in one block of memory. To find item `k`, Python computes
`start + k × slot_size` and jumps there: O(1). But inserting at the front means shifting **every**
item one slot to the right: O(n).

A `list` keeps spare room at the end so `append` is usually free. When it runs out, it allocates a
bigger block (about 1.125× the old size) and copies everything over. That's rare enough that it averages out to O(1).

A `tuple` is a fixed-size array that can't be changed. That makes it **hashable**, so it can be a dict
key or a set item, which is handy for records like `(user_id, name, title)`.

### Hash tables: `dict` and `set`

A hash function turns a key into a number, and that number picks a **bucket**. Looking up the key
means hashing it again and checking that bucket: O(1) on average, however much data there is.
That's why keys have to be **hashable**, meaning immutable. If a key could change after it was stored,
its hash would change too, and you'd never find it again.

You'll build one in `ch12_hashmaps/` (`key_to_index`, `insert`, ...).

## 5. Choosing: a quick decision guide

1. **"Do I look things up by a key/ID?"** Use a `dict`.
2. **"Do I only need to know *if* something is present, or remove duplicates?"** Use a `set`.
3. **"Does order or position matter, or do I need duplicates?"** Use a `list`.
4. **"Is it a fixed record that shouldn't change, or a compound key?"** Use a `tuple`.
5. **"Do I ask the same question many times?"** Pay O(n) once to build an **index** (`user_index/`).

## 6. Coming up next

The rest of the course builds the structures Python *doesn't* give you directly:

| Chapter | Structure | Superpower |
|---------|-----------|------------|
| 7  | Stack | last in, first out: undo, call stacks, bracket matching |
| 8  | Queue | first in, first out: task queues, BFS |
| 9  | Linked list | O(1) insert/remove at the ends: a faster queue |
| 10 | Binary tree | O(log n) search *and* insert, kept in order |
| 11 | Red-black tree | a binary tree that keeps itself balanced |
| 12 | Hash map | O(1) key lookup: the engine inside `dict` |
| 13 | Trie | prefix search: autocomplete |
| 14–15 | Graph, BFS/DFS | networks: "people you may know" |

Try this as a preview: `list.pop(0)` is O(n). Chapter 8 shows why that makes a list a bad queue, and
Chapter 9 fixes it.

## 7. Lessons in this chapter

Suggested order:

| Lesson | Structure | Function |
|--------|-----------|----------|
| `paginate_feed/` | list (indexing, slicing) | `get_page(posts, page, page_size)` |
| `job_title_counts/` | dict (counting) | `count_job_titles(users)` |
| `duplicate_handles/` | set (membership) | `find_duplicate_handles(handles)` |
| `mutual_connections/` | set (operations) | `get_mutual_connections(a, b)` |
| `user_index/` | dict of tuples (an index) | `build_user_index(users)`, `get_users_by_ids(index, ids)` |

## 8. Examples in this chapter

| File | What it shows |
|------|---------------|
| `examples/membership_timing.py` | `x in list` vs `x in set` vs `x in dict` as n grows |
| `examples/structure_tour.py` | mutability, hashability, ordering, and the shared-reference trap |

```bash
python ch06_data_structures_intro/examples/membership_timing.py
python ch06_data_structures_intro/examples/structure_tour.py
```
