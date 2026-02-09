## Hashmaps

### Overview
- **What is a Hashmap?**  
  A hashmap (also called hash table) is one of the most powerful and commonly used data structures in programming.  
  It provides **average-case O(1)** lookups, inserts, and deletes — dramatically faster than lists (O(n)) or binary search trees (O(log n)) for simple key-value access.

- **Real-world use in LockedIn**  
  - Looking up a user profile by username  
  - Checking if a username is already taken  
  - Storing session tokens → user mappings  
  - Counting occurrences (e.g., hashtag usage, follower stats)

- **Python reality check**  
  Python’s built-in `dict` **is** a hashmap — highly optimized and battle-tested.  
  In almost every real application, you should use `dict` instead of writing your own.  

  **But** — building a toy hashmap helps you deeply understand:
  - How hashing works under the hood
  - Why lookups are (usually) constant time
  - Collision handling (future topic)
  - Trade-offs between speed, memory, and simplicity

### Assignment: Build a Toy HashMap (Part 1 – Hash Function)

**Context**  
Binary search trees were too complex and slow for simple username → user profile lookups in LockedIn.  
Since the platform is small (CEO’s words: “business failure”), we can keep **all users in memory**.  
We don’t need ordering or range queries — just fast key-based access.

**Goal**  
Implement the `key_to_index` method of a simple `HashMap` class.  
This method is the **heart of the hash table**: it converts any string key (username) into a valid array index.

**What `key_to_index` must do**  
1. Take a string `key` (e.g., "alice123")
2. Compute the sum of the Unicode values of every character using `ord()`
3. Take that sum modulo (`%`) the size of the internal array (`self.size`)
4. Return the resulting integer index (0 to `self.size - 1`)

**Function Signature (inside HashMap class)**

```python
class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [None] * size   # We'll use this array to store data later

    def key_to_index(self, key: str) -> int:
        """
        Convert a string key into a valid array index using a simple hash function.
        
        Steps:
        1. Sum the Unicode values (ord) of every character in the key
        2. Take that sum modulo self.size to get an index in range [0, self.size-1]
        
        Args:
            key: The string key (e.g., username)
        
        Returns:
            int: Index where this key should be stored / looked up
        """
        # Your implementation here
        pass
```

### Step-by-Step: How to Implement `key_to_index`

1. Initialize a variable `total = 0`
2. Loop over every character in the string `key`:
   - Use `ord(char)` to get its Unicode integer value
   - Add that value to `total`
3. Compute `index = total % self.size`
4. Return `index`

**Example Walkthrough**
```python
key = "cat"
self.size = 10

ord('c') = 99
ord('a') = 97
ord('t') = 116

total = 99 + 97 + 116 = 312

index = 312 % 10 = 2

→ "cat" would be stored/looked up in bucket index 2
```

### Hints & Best Practices

- Use a simple `for char in key:` loop — strings are iterable in Python
- `ord()` works on any single character (returns an integer)
- Always use `self.size` (not a hardcoded number) — makes the class flexible
- No need to worry about negative numbers — `ord()` values are positive
- For now, **ignore collisions** — we’ll handle them in the next part
- Keep it clean and readable — future you will thank you

**Quick Test Cases to Think About**
- Empty string → sum = 0 → index = 0
- Very long username → large sum, but `% size` keeps it in bounds
- Keys that hash to same index (e.g., "cat" and "act") → collision (handled later)

### Learning Connections
- **Big-O Analysis**: Hash table operations are **O(1)** average case (assuming good hash function & low collisions)
- **Data Structures Intro**: This is the foundation of **Hashmaps** — the most-used structure after arrays and lists
- **Future topics**: Collision resolution (chaining, open addressing), load factor, resizing, better hash functions

**Next steps** (in future assignments):
- Store key-value pairs in buckets
- Handle collisions (chaining with lists)
- Implement `put`, `get`, `remove`

Start simple — get `key_to_index` working perfectly, then we’ll build the full hashmap!

Happy hashing! 🚀

## Solution and it's explanation:

```python
class HashMap:
    def key_to_index(self, key):
        """
        Convert a string key into a valid array index using a simple hash function.
        """
        total = 0
        for char in key:
            total += ord(char)
        return total % len(self.hashmap)
```

## Explained

**Dev: Yes, Exactly! Breaking Down the Character-by-Character Process**

---

## **TL;DR: Character Extraction & Unicode Conversion**

Yes! The code loops through the username string, extracts **each individual character** (letters, numbers, symbols), converts each to its **Unicode integer value**, and sums them up.

---

## **Visual Walkthrough**

### **Example: Username "Bob#7"**

```python
key = "Bob#7"
#     ↓ ↓ ↓ ↓ ↓
#     B o b # 7  ← Individual characters

# Loop iteration by iteration:

# Iteration 1:
char = 'B'
ord('B') = 66
total = 0 + 66 = 66

# Iteration 2:
char = 'o'
ord('o') = 111
total = 66 + 111 = 177

# Iteration 3:
char = 'b'
ord('b') = 98
total = 177 + 98 = 275

# Iteration 4:
char = '#'
ord('#') = 35
total = 275 + 35 = 310

# Iteration 5:
char = '7'
ord('7') = 55  # Note: This is the character '7', not the number 7
total = 310 + 55 = 365

# Final step:
index = 365 % 10 = 5  # Assuming hashmap size is 10

# Result: "Bob#7" maps to index 5
```

---

## **Character-by-Character Extraction**

### **How Python Iterates Over Strings:**

```python
username = "Alice"

# When you do:
for char in username:
    print(char)

# Python automatically extracts each character:
# Output:
# A
# l
# i
# c
# e

# Behind the scenes:
# char = username[0]  → 'A'
# char = username[1]  → 'l'
# char = username[2]  → 'i'
# char = username[3]  → 'c'
# char = username[4]  → 'e'
```

---

## **What `ord()` Does to Each Character**

### **Converting Characters to Numbers:**

```python
# Letters:
ord('A') = 65
ord('B') = 66
ord('Z') = 90

ord('a') = 97
ord('b') = 98
ord('z') = 122

# Numbers (as characters):
ord('0') = 48
ord('1') = 49
ord('9') = 57

# Symbols:
ord('#') = 35
ord('@') = 64
ord('_') = 95
ord(' ') = 32  # Space

# Emojis (yes, they work too!):
ord('🔥') = 128293
```

---

## **Real Example from Your Test File**

### **From `user.py`:**

```python
# File: /home/linux/Projects/BootDev/Dsa-Python/Ch12_Hashmaps/user.py

user_names = [
    "Blake",
    "Ricky",
    "Shelley",
    # ... more names
]
self.user_name = f"{user_names[id % len(user_names)]}#{id}"
#                                                      ↑
#                                                 Adds # and number
```

### **Example: User with ID 5**

```python
# User creation:
user = User(5)
# user.user_name = "George#5"  (assuming George is at index 5)

# Hash function processes it:
key = "George#5"

# Character extraction:
'G' → ord('G') = 71
'e' → ord('e') = 101
'o' → ord('o') = 111
'r' → ord('r') = 114
'g' → ord('g') = 103
'e' → ord('e') = 101
'#' → ord('#') = 35
'5' → ord('5') = 53

# Sum:
total = 71 + 101 + 111 + 114 + 103 + 101 + 35 + 53 = 689

# Map to index (if hashmap size is 10):
index = 689 % 10 = 9

# Result: User "George#5" stored at index 9
```

---

## **Why Extract Each Character?**

### **Goal: Convert String → Number**

```python
# Problem: Can't use strings as array indices
array[5]        # ✅ Valid
array["alice"]  # ❌ TypeError: list indices must be integers

# Solution: Convert string to integer
"alice" → [extract chars] → [unicode values] → [sum] → [modulo] → index
```

---

## **Step-by-Step Code Execution**

### **Annotated Version:**

```python
# File: /home/linux/Projects/BootDev/Dsa-Python/Ch12_Hashmaps/main.py

def key_to_index(self, key):
    total = 0  # Start with zero
    
    # Loop extracts each character one at a time
    for char in key:  # char = 'B', then 'o', then 'b', etc.
        # Convert character to its Unicode number
        unicode_value = ord(char)  # 66, 111, 98, etc.
        
        # Add to running total
        total += unicode_value  # 0+66=66, 66+111=177, 177+98=275, etc.
    
    # Wrap total into valid array range
    return total % len(self.hashmap)  # 365 % 10 = 5
```

---

## **Comparison: Different Usernames**

### **How Different Names Hash:**

```python
# Assuming hashmap size = 10

# Username: "A"
ord('A') = 65
total = 65
index = 65 % 10 = 5

# Username: "B"
ord('B') = 66
total = 66
index = 66 % 10 = 6

# Username: "AA"
ord('A') + ord('A') = 65 + 65 = 130
index = 130 % 10 = 0

# Username: "alice"
ord('a') + ord('l') + ord('i') + ord('c') + ord('e')
= 97 + 108 + 105 + 99 + 101 = 510
index = 510 % 10 = 0

# Username: "bob"
ord('b') + ord('o') + ord('b')
= 98 + 111 + 98 = 307
index = 307 % 10 = 7
```

---

## **What About Special Characters?**

### **They Work the Same Way:**

```python
# Username: "user@123"

'u' → ord('u') = 117
's' → ord('s') = 115
'e' → ord('e') = 101
'r' → ord('r') = 114
'@' → ord('@') = 64   # ← Special character
'1' → ord('1') = 49   # ← Digit character
'2' → ord('2') = 50
'3' → ord('3') = 51

total = 117 + 115 + 101 + 114 + 64 + 49 + 50 + 51 = 661
index = 661 % 10 = 1
```

---

## **Mental Model: String as a List of Characters**

```python
# Python treats strings as sequences of characters

username = "Bob"

# You can access individual characters:
username[0]  # → 'B'
username[1]  # → 'o'
username[2]  # → 'b'

# The for loop does this automatically:
for char in username:
    # First loop:  char = username[0] = 'B'
    # Second loop: char = username[1] = 'o'
    # Third loop:  char = username[2] = 'b'
    print(char)
```

---

## **Why This Works as a Hash Function**

### **Properties:**

1. **Deterministic**: Same input always gives same output
   ```python
   key_to_index("alice") → Always returns same index
   ```

2. **Distributes keys**: Different strings usually map to different indices
   ```python
   "alice" → index 0
   "bob"   → index 7
   "carol" → index 3
   ```

3. **Fast**: O(n) where n = length of string (very fast for short usernames)

4. **Simple**: Easy to understand and implement

---

## **Collision Example**

### **When Different Keys Map to Same Index:**

```python
# These two different usernames might hash to the same index:

# Username 1: "abc"
ord('a') + ord('b') + ord('c') = 97 + 98 + 99 = 294
index = 294 % 10 = 4

# Username 2: "bac" (same letters, different order)
ord('b') + ord('a') + ord('c') = 98 + 97 + 99 = 294
index = 294 % 10 = 4  # ← Same index! This is a collision

# This is why hashmaps need collision handling (future topic)
```

---

## **Summary**

✅ **Yes** The code:

1. **Extracts each character** from the username string
2. **Converts each to Unicode** using `ord()`
3. **Sums all the values** together
4. **Uses modulo** to fit the sum into a valid array index

It's a simple but effective way to turn any string into a number that can be used as an array index!


## This Hashmap function example and Big O Notation

**Dev: Big-O Analysis of Hash Function – O(n), Not O(1)**

---

## **TL;DR: This Hash Function is O(n), Not O(1)**

The `key_to_index` function has **O(n)** time complexity, where **n = length of the key string**. It must process every character in the input, so longer keys take proportionally longer.

---

## **Why It's O(n)**

### **Code Analysis:**

```python
# File: /home/linux/Projects/BootDev/Dsa-Python/Ch12_Hashmaps/main.py

def key_to_index(self, key):
    total = 0                    # O(1) - constant time
    for char in key:             # O(n) - loops n times (n = len(key))
        total += ord(char)       # O(1) - constant time per iteration
    return total % len(self.hashmap)  # O(1) - constant time

# Overall: O(1) + O(n) × O(1) + O(1) = O(n)
```

### **Step-by-Step Breakdown:**

```python
# Example: key = "alice" (5 characters)

total = 0                    # 1 operation
for char in key:             # Loop runs 5 times
    total += ord(char)       # 2 operations per loop (ord + addition)
return total % len(self.hashmap)  # 2 operations (len + modulo)

# Total operations: 1 + (5 × 2) + 2 = 13 operations
# This scales linearly with key length → O(n)
```

---

## **Comparison: Different Key Lengths**

### **How Runtime Scales:**

```python
# Key length 1:
key = "a"
# Loop runs: 1 time
# Operations: ~3

# Key length 5:
key = "alice"
# Loop runs: 5 times
# Operations: ~13

# Key length 10:
key = "superadmin"
# Loop runs: 10 times
# Operations: ~23

# Key length 100:
key = "a" * 100  # Very long username
# Loop runs: 100 times
# Operations: ~203

# Pattern: Operations ≈ 2n + 3 → O(n)
```

---

## **Visual: O(n) Growth**

```
Operations
    │
200 │                                    ●
    │
150 │
    │
100 │                          ●
    │
 50 │              ●
    │
  0 │    ●
    └─────────────────────────────────────── Key Length (n)
         1        10       50      100

Linear growth → O(n) complexity
```

---

## **Why Hashmap Operations Are Still O(1) Overall**

### **Important Distinction:**

```python
# The hash function itself: O(n)
index = hm.key_to_index("alice")  # O(n) where n = len("alice") = 5

# BUT: Hashmap operations are considered O(1) because:
# 1. Username lengths are bounded (typically < 50 characters)
# 2. n is the key length, NOT the hashmap size
# 3. In Big-O analysis, we treat bounded inputs as constants

# Example:
hm = HashMap(1000000)  # 1 million slots
hm.key_to_index("alice")  # Still only processes 5 characters
#                            Not affected by hashmap size!
```

---

## **Big-O in Context: What We're Measuring**

### **Two Different "n" Values:**

```python
# Scenario 1: Hash function complexity
# n = length of the key string
def key_to_index(self, key):
    for char in key:  # Loops len(key) times
        total += ord(char)
    return total % len(self.hashmap)
# Complexity: O(len(key)) = O(n)

# Scenario 2: Hashmap lookup complexity
# n = number of items in the hashmap
def get(self, key):
    index = self.key_to_index(key)  # O(len(key))
    return self.hashmap[index]      # O(1) array access
# Complexity: O(len(key)) ≈ O(1) if key length is bounded
```

---

## **Why We Say Hashmaps Are O(1)**

### **Practical Assumptions:**

```python
# In real-world usage:

# ✅ Key lengths are bounded
usernames = ["alice", "bob123", "admin"]  # All < 20 chars
# Processing 5-20 characters is effectively constant time

# ✅ Key length doesn't grow with data size
hm = HashMap(10)
hm.put("alice", user1)  # Processes 5 chars

hm = HashMap(1000000)
hm.put("alice", user1)  # Still processes 5 chars (not 1M!)

# ✅ Comparison to alternatives
# Binary Search Tree: O(log n) where n = number of items
# Hashmap: O(k) where k = key length (bounded constant)
# 
# If k is bounded (e.g., k ≤ 50), then O(k) ≈ O(1)
```

---

## **Formal Big-O Statement**

### **Precise Analysis:**

```python
# Hash function: O(k) where k = key length
def key_to_index(self, key):
    # Time: O(k)
    # Space: O(1)
    pass

# Hashmap operations (assuming no collisions):
def put(self, key, value):
    index = self.key_to_index(key)  # O(k)
    self.hashmap[index] = value     # O(1)
    # Total: O(k)

def get(self, key):
    index = self.key_to_index(key)  # O(k)
    return self.hashmap[index]      # O(1)
    # Total: O(k)

# Where k is bounded by max username length (e.g., 50)
# So O(k) ≈ O(1) in practice
```

---

## **Comparison: True O(1) vs O(n)**

### **Example 1: True O(1) Operation**

```python
# File: /home/linux/Projects/BootDev/Dsa-Python/ChapterThree/big-0-examples/tim_one.py

def example_one(num):
    return num % 2 == 0
    # Always 1 operation, regardless of input size
    # True O(1)
```

### **Example 2: O(n) Operation (Your Hash Function)**

```python
def key_to_index(self, key):
    total = 0
    for char in key:  # n iterations
        total += ord(char)
    return total % len(self.hashmap)
    # Operations scale with len(key)
    # O(n) where n = len(key)
```

---

## **What If We Wanted True O(1) Hashing?**

### **Hypothetical (Impractical) Approach:**

```python
# To get O(1), we'd need to hash without looping:

def key_to_index_constant(self, key):
    # Only look at first character (ignores rest)
    if len(key) == 0:
        return 0
    return ord(key[0]) % len(self.hashmap)
    # O(1) - but terrible hash function!
    # "alice" and "admin" both hash to same index

# Why this is bad:
# - Ignores most of the key
# - Massive collisions
# - Defeats purpose of hashing
```

---

## **Real-World Hash Functions**

### **Python's Built-in `hash()`:**

```python
# Python's hash() is also O(n) for strings
hash("alice")  # Processes all characters
hash("a" * 1000)  # Takes longer than hash("a")

# But it's optimized and still very fast:
import timeit

# Short string:
timeit.timeit(lambda: hash("alice"), number=1000000)
# ~0.02 seconds for 1M hashes

# Long string:
timeit.timeit(lambda: hash("a" * 100), number=1000000)
# ~0.15 seconds for 1M hashes (longer, but still fast)
```

---

## **Summary Table**

| Operation | Complexity | Explanation |
|-----------|------------|-------------|
| `key_to_index(key)` | **O(k)** | k = length of key string |
| Array access `hashmap[i]` | **O(1)** | Direct index lookup |
| Hashmap `get(key)` | **O(k) ≈ O(1)** | Hash + array access (k bounded) |
| Hashmap `put(key, val)` | **O(k) ≈ O(1)** | Hash + array write (k bounded) |

**Where:**
- **k** = key length (typically bounded, e.g., ≤ 50 chars)
- **n** = number of items in hashmap (irrelevant to hash function)

---

## **Key Takeaway**

✅ **Technically**: The hash function is **O(n)** where n = key length

✅ **Practically**: Hashmap operations are **O(1)** because:
- Key lengths are bounded (constant upper limit)
- Hash time doesn't depend on hashmap size
- O(bounded constant) = O(1) in Big-O analysis

This is why hashmaps are considered **constant-time** data structures, even though the hash function itself loops through the key!


