**Dev: Algorithm Analysis – O(nm) Name Counting Challenge**

---

## **Understanding the Assignment**

### **What You're Building:**
A function that counts how many times a specific name appears across **multiple lists of names**.

### **The Complexity Challenge:**
This is an **O(nm)** problem:
- **n** = number of influencers (outer lists)
- **m** = average number of names per influencer (inner list length)

You must iterate through **every name in every list** to count occurrences.

---

## **Breaking Down the Problem**

### **Input Structure:**
```python
all_names = [
    ["George", "Eva", "George"],           # Influencer 1's list
    ["Diane", "George", "Eva", "Frank"],   # Influencer 2's list
    ["Diane", "George"]                    # Influencer 3's list
]
target = "George"
```

### **Expected Output:**
```python
# Count all occurrences of "George" across ALL lists
# Influencer 1: 2 times
# Influencer 2: 1 time
# Influencer 3: 1 time
# Total: 4
```

---

## **Visual Representation**

```
Input: all_names = [
    ["George", "Eva", "George"],        ← List 1 (3 names)
    ["Diane", "George", "Eva", "Frank"], ← List 2 (4 names)
    ["Diane", "George"]                  ← List 3 (2 names)
]
target = "George"

Step-by-step traversal:
┌─────────────────────────────────────┐
│ List 1: ["George", "Eva", "George"] │
│         ↑ match!       ↑ match!     │
│         count = 1      count = 2    │
└─────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ List 2: ["Diane", "George", "Eva", "Frank"] │
│                   ↑ match!                │
│                   count = 3               │
└──────────────────────────────────────────┘

┌─────────────────────────┐
│ List 3: ["Diane", "George"] │
│                 ↑ match!    │
│                 count = 4   │
└─────────────────────────┘

Final count: 4
```

---

## **Pseudo Code (High-Level)**

```
FUNCTION count_names(all_names, target):
    1. Initialize a counter to 0
    
    2. FOR EACH list in all_names:  ← Outer loop (n times)
        3. FOR EACH name in current list:  ← Inner loop (m times)
            4. IF name equals target:
                5. Increment counter
    
    6. RETURN counter
```

---

## **Simpler Analogous Problem (Template)**

### **Problem: Count Apples in Multiple Baskets**

```python
def count_apples(baskets):
    """
    Count total apples across all baskets.
    
    baskets = [
        ["apple", "orange", "apple"],    # Basket 1
        ["banana", "apple"],             # Basket 2
        ["orange", "orange"]             # Basket 3
    ]
    
    Expected output: 3 (total apples)
    """
    total_apples = 0  # Step 1: Initialize counter
    
    # Step 2: Loop through each basket (outer loop)
    for basket in baskets:
        
        # Step 3: Loop through each fruit in current basket (inner loop)
        for fruit in basket:
            
            # Step 4: Check if it's an apple
            if fruit == "apple":
                total_apples += 1  # Step 5: Increment
    
    return total_apples  # Step 6: Return result


# Test it:
baskets = [
    ["apple", "orange", "apple"],
    ["banana", "apple"],
    ["orange", "orange"]
]

result = count_apples(baskets)
print(result)  # Output: 3
```

---

## **How This Maps to Your Problem**

| Apples Problem | Your Problem |
|----------------|--------------|
| `baskets` | `all_names` |
| `basket` | `names_list` (one influencer's list) |
| `fruit` | `name` (one person's name) |
| `"apple"` | `target` (the name you're searching for) |
| `total_apples` | `count` (your counter variable) |

---

## **Step-by-Step Hints**

### **Hint 1: Function Signature**
```python
def count_names(all_names, target):
    # Your code here
    pass
```

**What you receive:**
- `all_names`: A list of lists (like `baskets`)
- `target`: A string (the name to count)

---

### **Hint 2: Initialize Your Counter**
```python
def count_names(all_names, target):
    count = 0  # Start counting from zero
    # ... rest of your code
```

**Why?** You need somewhere to accumulate the total.

---

### **Hint 3: Outer Loop Structure**
```python
def count_names(all_names, target):
    count = 0
    
    for names_list in all_names:  # Loop through each influencer's list
        # Now you have ONE list of names
        # Next: loop through THIS list
```

**What `names_list` represents:**
- First iteration: `["George", "Eva", "George"]`
- Second iteration: `["Diane", "George", "Eva", "Frank"]`
- And so on...

---

### **Hint 4: Inner Loop Structure**
```python
def count_names(all_names, target):
    count = 0
    
    for names_list in all_names:
        for name in names_list:  # Loop through each name in current list
            # Now you have ONE name (a string)
            # Next: check if it matches target
```

**What `name` represents:**
- First inner iteration: `"George"`
- Second inner iteration: `"Eva"`
- Third inner iteration: `"George"`
- And so on...

---

### **Hint 5: Comparison Logic**
```python
def count_names(all_names, target):
    count = 0
    
    for names_list in all_names:
        for name in names_list:
            if name == target:  # Does this name match what we're looking for?
                # If yes, do something with count
```

**Question to ask yourself:** What should happen to `count` when you find a match?

---

### **Hint 6: Return Statement**
```python
def count_names(all_names, target):
    count = 0
    
    for names_list in all_names:
        for name in names_list:
            if name == target:
                # ... increment count here
    
    return count  # Don't forget to return the final result!
```

---

## **Test Case Walkthrough**

### **Example from `main_test.py`:**
```python
all_names = [
    ["George", "Eva", "George"],
    ["Diane", "George", "Eva", "Frank"]
]
target = "George"
expected = 3
```

### **Manual Trace:**
```
Outer Loop Iteration 1:
  names_list = ["George", "Eva", "George"]
  
  Inner Loop Iteration 1:
    name = "George"
    "George" == "George"? YES → count = 1
  
  Inner Loop Iteration 2:
    name = "Eva"
    "Eva" == "George"? NO → count = 1 (unchanged)
  
  Inner Loop Iteration 3:
    name = "George"
    "George" == "George"? YES → count = 2

Outer Loop Iteration 2:
  names_list = ["Diane", "George", "Eva", "Frank"]
  
  Inner Loop Iteration 1:
    name = "Diane"
    "Diane" == "George"? NO → count = 2
  
  Inner Loop Iteration 2:
    name = "George"
    "George" == "George"? YES → count = 3
  
  Inner Loop Iteration 3:
    name = "Eva"
    "Eva" == "George"? NO → count = 3
  
  Inner Loop Iteration 4:
    name = "Frank"
    "Frank" == "George"? NO → count = 3

Final count: 3 ✓
```

---

## **Edge Cases to Consider**

### **1. Empty Input**
```python
all_names = []
target = "George"
# Expected: 0 (no lists to search)
```

**Your loop should handle this automatically** (loop never executes).

---

### **2. Target Not Found**
```python
all_names = [["Alice", "Bob"], ["Charlie", "Diana"]]
target = "George"
# Expected: 0 (George doesn't appear)
```

**Your counter stays at 0** (no matches found).

---

### **3. Empty Inner Lists**
```python
all_names = [[], ["George"], []]
target = "George"
# Expected: 1 (only one George in the middle list)
```

**Your inner loop handles empty lists** (skips them).

---

### **4. Multiple Occurrences in Same List**
```python
all_names = [["George", "George", "George"]]
target = "George"
# Expected: 3 (count each occurrence)
```

**Your counter increments for EACH match** (not just once per list).

---

## **Common Mistakes to Avoid**

### **❌ Mistake 1: Counting Lists Instead of Names**
```python
# WRONG:
for names_list in all_names:
    if target in names_list:
        count += 1  # This only counts "does the list contain George?"
                    # Not "how many times does George appear?"
```

**Why wrong?** `["George", "George"]` would only count as 1, not 2.

---

### **❌ Mistake 2: Forgetting to Return**
```python
def count_names(all_names, target):
    count = 0
    for names_list in all_names:
        for name in names_list:
            if name == target:
                count += 1
    # Oops! Forgot to return count
```

**Fix:** Add `return count` at the end.

---

### **❌ Mistake 3: Returning Inside the Loop**
```python
def count_names(all_names, target):
    count = 0
    for names_list in all_names:
        for name in names_list:
            if name == target:
                count += 1
                return count  # WRONG! Returns too early
```

**Why wrong?** This returns after finding the FIRST match, not counting all of them.

---

## **Complexity Analysis (For Your Understanding)**

### **Time Complexity: O(nm)**
```python
for names_list in all_names:      # Runs n times (n = number of lists)
    for name in names_list:        # Runs m times (m = avg names per list)
        if name == target:         # O(1) comparison
            count += 1             # O(1) operation
```

**Total:** n × m × O(1) = **O(nm)**

---

### **Space Complexity: O(1)**
```python
count = 0  # Only one variable (constant space)
```

**No extra data structures needed** (just a counter).

---

## **Template Structure (Fill in the Blanks)**

```python
# File: /home/linux/Projects/BootDev/Dsa-Python/ChapterThree/Name_Count/main.py

def count_names(all_names, target):
    """
    Count occurrences of target name across all lists.
    
    Time Complexity: O(nm) where:
      n = number of lists
      m = average length of each list
    
    Space Complexity: O(1) - only uses a counter variable
    """
    # Step 1: Initialize counter
    count = ___
    
    # Step 2: Outer loop - iterate through each list
    for ___ in ___:
        
        # Step 3: 
```