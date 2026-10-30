### Assignment: Implementing the "Find Minimum" Algorithm for LockedIn

In this course, we're building components of a fictional social network called LockedIn. LockedIn is a platform where professionals can showcase how their for-profit work is actually driven by altruistic goals—imagine a mix of Facebook and a job fair. It also includes features for influencers to monitor their growth and engagement.

One key feature we need is to **help users identify the accounts they follow that have the lowest follower counts.** This allows them to spot less popular follows that might not be "worth" keeping anymore. To support this, you'll implement a simple "find minimum" algorithm in Python.


**Your task** 

- is to complete the `find_minimum()` function. 

- It takes a single argument: a list of integers called `nums` (representing follower counts). 

- The function should return the smallest number in the list. If the list is empty, it should return `None`.

#### Step-by-Step Instructions to Implement the Function:

1. **Initialize the minimum value**: 
Start by setting a variable called `minimum` to positive infinity using `float("inf")`. 
This ensures that any number in the list will be smaller than this initial value.

2. **Handle the empty list case**: 
Check if the list `nums` is empty (i.e., its length is 0). 
If it is, immediately return `None` since there's no minimum to find.

3. **Iterate through the list**: 
Use a loop to go through each number in the list `nums`. For each number:
   - Compare it to the current value of `minimum`.
   - If the number is smaller than `minimum`, update `minimum` to be that number.

4. **Return the result**: After the loop finishes, `minimum` will hold the smallest number in the list. Return this value.

#### Example Function Skeleton (to Complete):
```python
def find_minimum(nums):
    # Step 1: Initialize minimum here
    
    # Step 2: Check for empty list here
    
    # Step 3: Loop through nums and update minimum here
    
    # Step 4: Return the minimum here
```

#### Tips for Testing:
- Test with a sample list like `[10, 5, 20, 3]`—should return `3`.
- Test with an empty list `[]`—should return `None`.
- Test with a single-element list like `[42]`—should return `42`.
- Test with negative numbers like `[-1, -5, 0]`—should return `-5`.

This step-by-step approach ensures the algorithm is efficient (O(n) time complexity) and handles edge cases properly. Once implemented, this can be used to find the lowest follower count among followed accounts in LockedIn! If you need help with code examples or variations, let me know.

### Boot.Dev's solution
```python

def find_minimum(nums):
    # Step 1: Initialize minimum here
    minimum = float("inf")
    
    # Step 2: Check for empty list here
    if len(nums) == 0:
        return None
    
    # Step 3: Loop through nums and update minimum here
    for num in nums:
        if num < minimum:
            minimum = num
    
    # Step 4: Return the minimum here
    return minimum

```

### My solution
```python

def find_minimum(nums):
    if not nums:
        return None
    return min(nums)

```



