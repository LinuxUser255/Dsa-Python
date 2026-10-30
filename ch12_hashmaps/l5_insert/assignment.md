## Hashmaps

### Insert – Storing Key-Value Pairs

#### Overview
Now that we have a working hash function (`key_to_index`) to map any string key to a valid array index, the next step is to actually **store** data in the hashmap.

This is the **insert** operation — the fundamental way we add or update entries in a hash table.

- **What insert does**:
  - Takes a key (string, e.g., username) and a value (e.g., user profile object)
  - Computes the correct bucket index using the hash function
  - Places the key-value pair at that index in the internal array

- **Current limitation (this stage)**:
  We are **not yet handling collisions**.  
  If two different keys hash to the same index, the later insert will overwrite the earlier one.  
  (Collision resolution — chaining with linked lists or open addressing — comes in the next part.)

- **Goal for this assignment**:
  Get basic insertion working cleanly so the structure starts to behave like a real hashmap (even with the collision weakness for now).

#### Assignment

**Complete the `insert` method** in the `HashMap` class.

It should:

1. Convert the incoming `key` (string) to the correct storage index using `self.key_to_index(key)`
2. Create a key-value pair as a **tuple**: `(key, value)`
3. Store that tuple directly at the calculated index in `self.buckets`
4. If something already exists at that index, overwrite it (for now — collisions will be addressed later)

**Resulting internal structure** (example after a few inserts):

```text
self.buckets = [
    None,
    ("alice123", <User object>),
    None,
    ("bob_smith", <User object>),
    None,
    ("catlover99", <User object>),
    ...
]
```

- Indexes with data contain a `(key, value)` tuple  
- Empty indexes contain `None`

**Function Signature**

```python
class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [None] * size

    def key_to_index(self, key: str) -> int:
        # (already implemented from previous step)
        pass

    def insert(self, key: str, value) -> None:
        """
        Insert or update a key-value pair in the hashmap.
        
        For now: overwrites if the same index is already used (collision).
        
        Args:
            key:   string (e.g., username)
            value: any object (e.g., User profile)
        
        Returns:
            None (modifies internal buckets in place)
        
        Time Complexity (average): O(1)  [assuming good hash distribution]
        Space Complexity: O(1) per insert (excluding the value itself)
        """
        # Your implementation here
        pass
```

#### How It Works (Step-by-Step)

1. **Hash the key**  
   `index = self.key_to_index(key)`

2. **Create the pair**  
   `pair = (key, value)`

3. **Store it**  
   `self.buckets[index] = pair`

That’s it — three lines of logic for basic insertion!

**Example Walkthrough**
```python
hm = HashMap(size=10)

hm.insert("alice", User(name="Alice"))
# → computes index (say 3), stores ("alice", User) at buckets[3]

hm.insert("bob", User(name="Bob"))
# → different index (say 7), stores at buckets[7]

hm.insert("cat", User(name="CatLover"))
# → might collide with "alice" (say index 3 again) → overwrites Alice
```

#### Hints for Solving

- Call `self.key_to_index(key)` — don’t rewrite the hashing logic
- Use a simple tuple: `(key, value)`
- Assignment is straightforward: `self.buckets[index] = (key, value)`
- No return value needed → method modifies the object in place
- Don’t worry about checking if the key already exists (for now — that comes with proper `get` and collision handling)
- Keep the method short and readable — 3–5 lines is plenty

#### Learning Connections

- **Big-O Analysis**  
  - Average case: **O(1)** insert (constant time)  
  - Worst case (many collisions): **O(n)** — but we’ll fix that later with chaining

- **Hashmaps**  
  This is the second core operation (after hashing).  
  Insert + Get + (later) Delete = the classic hash table API.

- **Next steps in the series**:
  - Implement `get(key)` → retrieve value by key
  - Handle collisions (chaining: each bucket becomes a list)
  - Add basic resizing when load factor gets too high
  - Compare to Python’s `dict` (which does all of this internally)

Once `insert` works, you’ll have a minimal (but very fast — until collisions pile up) working hashmap!

Test it by inserting a few usernames and printing `hm.buckets` to see where things land.
