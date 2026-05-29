def find_max(nums):
    """take a list of integers and returns the maximum value"""

    if not nums:  # Check if list is empty
        return None  # Skipped (list is not empty)

    max_value = nums[0]  # Initialize max_value with first element in nums

    for num in nums[1:]:  # nums[1:] creates a slice: [4, 3, 100, 2343243, 343434, 1, 2, 32]
        if num > max_value:
            max_value = num

    return max_value





