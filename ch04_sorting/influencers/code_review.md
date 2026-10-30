**Dev: Python Testing Pattern – Object Creation in Test Files**

---

## **TL;DR: Yes, The objects are created in `main_test.py`**

The test file (`main_test.py`) creates `Influencer` objects and passes them to your functions. Your job in `main.py` is to implement the logic that **operates on** those pre-created objects.

---

## **How the Test-Implementation Pattern Works**

### **Flow Diagram:**
```
┌─────────────────────────────────────────────────────────────┐
│ main_test.py (Test File)                                    │
├─────────────────────────────────────────────────────────────┤
│ 1. Import your code:                                        │
│    from main import *                                       │
│                                                             │
│ 2. Create test objects:                                     │
│    theprimeagen = Influencer(100, 1)                        │
│    pokimane = Influencer(800, 2)                            │
│                                                             │
│ 3. Call YOUR functions with those objects:                  │
│    result = vanity(theprimeagen)                            │
│    sorted_list = vanity_sort([theprimeagen, pokimane])      │
│                                                             │
│ 4. Check if results match expectations:                     │
│    if result == expected_output:                            │
│        print("Pass")                                        │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ main.py (Your Implementation)                               │
├─────────────────────────────────────────────────────────────┤
│ class Influencer:                                           │
│     # Class definition (already provided)                   │
│                                                             │
│ def vanity(influencer):                                     │
│     # YOU implement this                                    │
│     # Receives: influencer object (e.g., theprimeagen)      │
│     # Returns: vanity score (int)                           │
│                                                             │
│ def vanity_sort(influencers):                               │
│     # YOU implement this                                    │
│     # Receives: list of influencer objects                  │
│     # Returns: sorted list                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## **Breaking Down the Test File**

### **From `main_test.py`:**
```python
# File: /home/linux/Projects/BootDev/Dsa-Python/CH4-SortingAlgos/influencers/main_test.py

# Step 1: Import everything from your main.py
from main import *  # Gets: Influencer class, vanity(), vanity_sort()

# Step 2: Create test objects using YOUR Influencer class
theprimeagen = Influencer(100, 1)  # num_selfies=100, num_bio_links=1
pokimane = Influencer(800, 2)      # num_selfies=800, num_bio_links=2
spambot = Influencer(0, 200)       # num_selfies=0, num_bio_links=200
lane = Influencer(10, 2)           # num_selfies=10, num_bio_links=2
badcop = Influencer(1, 2)          # num_selfies=1, num_bio_links=2

# Step 3: Test cases (list of tuples)
run_cases = [
    # Each tuple is: (input, expected_output)
    # Format: (list_of_influencers, expected_sorted_list)
    ([theprimeagen, pokimane], [theprimeagen, pokimane]),  # Example test
    # ... more test cases
]

# Step 4: Test execution
def do_test(input1, expected_output):
    result = vanity_sort(input1)  # ← Calls YOUR function
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False
```

---

## **What Each Test Object Represents**

### **Visual Breakdown:**
```python
# Object creation syntax:
# Influencer(num_selfies, num_bio_links)
#            ↑            ↑
#            1st arg      2nd arg

theprimeagen = Influencer(100, 1)
# Creates an object with:
#   theprimeagen.num_selfies = 100
#   theprimeagen.num_bio_links = 1

pokimane = Influencer(800, 2)
# Creates an object with:
#   pokimane.num_selfies = 800
#   pokimane.num_bio_links = 2

spambot = Influencer(0, 200)
# Creates an object with:
#   spambot.num_selfies = 0
#   spambot.num_bio_links = 200
```

---

## **How Your Functions Receive These Objects**

### **Example 1: `vanity()` Function**
```python
# In main_test.py:
theprimeagen = Influencer(100, 1)
score = vanity(theprimeagen)  # ← Passes object to your function

# In main.py (your implementation):
def vanity(influencer):
    # 'influencer' parameter now holds the theprimeagen object
    # You can access:
    #   influencer.num_selfies    → 100
    #   influencer.num_bio_links  → 1
    
    # Your job: calculate and return the vanity score
    pass
```

---

### **Example 2: `vanity_sort()` Function**
```python
# In main_test.py:
theprimeagen = Influencer(100, 1)
pokimane = Influencer(800, 2)
lane = Influencer(10, 2)

test_list = [theprimeagen, pokimane, lane]
sorted_result = vanity_sort(test_list)  # ← Passes list to your function

# In main.py (your implementation):
def vanity_sort(influencers):
    # 'influencers' parameter now holds the list:
    # [theprimeagen, pokimane, lane]
    
    # You can iterate through it:
    # for influencer in influencers:
    #     influencer.num_selfies
    #     influencer.num_bio_links
    
    # Your job: return a NEW sorted list
    pass
```

---

## **Calculating Vanity Scores (Manual Example)**

### **Given Objects:**
```python
theprimeagen = Influencer(100, 1)  # num_selfies=100, num_bio_links=1
pokimane = Influencer(800, 2)      # num_selfies=800, num_bio_links=2
spambot = Influencer(0, 200)       # num_selfies=0, num_bio_links=200
```

### **Formula (from Assignment):**
```
vanity_score = (num_bio_links × 5) + num_selfies
```

### **Manual Calculations:**
```python
# theprimeagen:
vanity = (1 × 5) + 100
       = 5 + 100
       = 105

# pokimane:
vanity = (2 × 5) + 800
       = 10 + 800
       = 810

# spambot:
vanity = (200 × 5) + 0
       = 1000 + 0
       = 1000
```

### **Expected Sort Order (Ascending):**
```python
# Sorted by vanity score (lowest to highest):
[
    theprimeagen,  # vanity = 105
    spambot,       # vanity = 1000
    pokimane       # vanity = 810... wait, that's wrong!
]

# Actually:
[
    theprimeagen,  # vanity = 105
    pokimane,      # vanity = 810
    spambot        # vanity = 1000
]
```

---

## **How to Access Object Attributes in Your Functions**

### **Pattern:**
```python
def vanity(influencer):
    # Access attributes using dot notation:
    selfies = influencer.num_selfies      # Gets the num_selfies value
    links = influencer.num_bio_links      # Gets the num_bio_links value
    
    # Use them in calculations:
    score = (links * 5) + selfies
    
    return score
```

### **Example with Real Object:**
```python
# Test creates:
theprimeagen = Influencer(100, 1)

# Your function receives it:
def vanity(influencer):
    # influencer is now theprimeagen
    # influencer.num_selfies → 100
    # influencer.num_bio_links → 1
    
    score = (influencer.num_bio_links * 5) + influencer.num_selfies
    #       (1 * 5) + 100
    #       = 105
    
    return score  # Returns 105
```

---

## **Common Mistakes to Avoid**

### **❌ Mistake 1: Trying to Create Objects in Your Functions**
```python
# WRONG - Don't do this:
def vanity(influencer):
    obj = Influencer(100, 1)  # ❌ Don't create new objects
    return obj.num_bio_links * 5 + obj.num_selfies
```

**Why wrong?** The test already created the object and passed it to you. Use the `influencer` parameter!

---

### **❌ Mistake 2: Using Wrong Attribute Names**
```python
# WRONG - Attribute names don't match:
def vanity(influencer):
    return influencer.bio_links * 5 + influencer.selfies  # ❌ Missing 'num_'
```

**Correct attribute names:**
- `influencer.num_selfies` ✅
- `influencer.num_bio_links` ✅

---

### **❌ Mistake 3: Hardcoding Values**
```python
# WRONG - Don't hardcode:
def vanity(influencer):
    return 105  # ❌ Only works for theprimeagen!
```

**Why wrong?** Your function must work for **any** influencer object, not just one specific case.

---

### **❌ Mistake 4: Modifying the Original List**
```python
# WRONG - Don't modify in place:
def vanity_sort(influencers):
    influencers.sort(key=vanity)  # ❌ Modifies original list
    return influencers
```

**Why wrong?** Assignment says "return a **new** list". Use `sorted()` (creates new list), not `.sort()` (modifies in place).

---

## **Step-by-Step Implementation Guide**

### **Step 1: Implement `vanity()` First**
```python
def vanity(influencer):
    # 1. Access the two attributes you need
    links = influencer.num_bio_links
    selfies = influencer.num_selfies
    
    # 2. Apply the formula
    score = (links * 5) + selfies
    
    # 3. Return the result
    return score
```

**Test it mentally:**
```python
# If theprimeagen = Influencer(100, 1):
links = 1
selfies = 100
score = (1 * 5) + 100 = 105 ✓
```

---

### **Step 2: Implement `vanity_sort()` Using `vanity()`**
```python
def vanity_sort(influencers):
    # Use sorted() with key parameter
    # The key tells sorted() HOW to compare objects
    
    return sorted(influencers, key=vanity)
    #      ↑                      ↑
    #      Creates new list       Uses your vanity() function
```

**How `key=vanity` works:**
```python
# sorted() internally does this for each influencer:
# 1. Call vanity(influencer1) → get score1
# 2. Call vanity(influencer2) → get score2
# 3. Compare score1 vs score2
# 4. Sort based 
```