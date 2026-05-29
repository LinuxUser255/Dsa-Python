# Assignment

LockedIn users want to know which of their followers has the highest engagement score.

Complete the find_max function. It should take a list of integers and return the largest value in the list.

The "runtime complexity" (aka Big O) of this function should be O(n).



## My solution
```python
def find_max(nums):
    """take a list of integers and returns the maximum value"""

    if not nums:  # Check if list is empty
        return None  # Skipped (list is not empty)

    max_value = nums[0]  # Initialize max_value with first element in nums

    for num in nums[1:]:  # nums[1:] creates a slice: [4, 3, 100, 2343243, 343434, 1, 2, 32]
        if num > max_value:
            max_value = num

    return max_value
```

## Boot.Dev's solution
```python

def find_max(nums):
    highest = float("-inf")
    for num in nums:  # nums[1:] creates a slice: [4, 3, 100, 2343243, 343434, 1, 2, 32]
        if num > highest:
            highest = num

    return highest

```