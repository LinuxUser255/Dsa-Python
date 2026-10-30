# Lists: Paginate a Feed

A Python `list` is a **dynamic array**: its items sit in one block of memory, side by side.
That's why `posts[1_999_800]` is **O(1)**. Python works out exactly where item `k` lives
(start address + k × slot size) and jumps straight there, without walking past the items before it.

| List operation | Big-O | Why |
|----------------|-------|-----|
| `nums[i]`, `nums[i] = x` | O(1) | jump straight to the slot |
| `nums.append(x)` | O(1) on average | add to the end; occasionally grows the array |
| `nums.pop()` | O(1) | remove from the end |
| `nums.insert(0, x)`, `nums.pop(0)` | O(n) | every other item has to shift over |
| `x in nums` | O(n) | has to check items one by one |
| `nums[a:b]` | O(b - a) | copies just that slice |

## Assignment

LockedIn's feed can hold millions of posts, but the app only shows a few at a time.
Complete `get_page(posts, page, page_size)`, which returns the posts for one **page** of the feed.

- `page` starts at **1**. Page 1 is the first `page_size` posts, page 2 the next `page_size`, and so on.
- The last page may be shorter than `page_size`.
- A page past the end of the feed returns `[]`.
- A `page` of `0` or lower is invalid: return `[]`.

### Example

```python
posts = ["post1", "post2", ..., "post10"]
get_page(posts, 1, 3)  # ["post1", "post2", "post3"]
get_page(posts, 4, 3)  # ["post10"]
get_page(posts, 5, 3)  # []
```

### The catch

The last submit case asks for page 19,999 of a **2,000,000**-post feed, with a **20 millisecond** limit.
Walking through the feed counting posts until you reach the right page won't make it.
Your solution should take time proportional to `page_size`, not to the size of the feed.
