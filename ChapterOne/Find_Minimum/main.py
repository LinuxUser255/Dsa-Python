def find_minimum(nums):
    """thes numbers are referenced here are in the main_test.py file"""
    # nums = [7, 4, 3, 100, 2343243, 343434, 1, 2, 32]

    if not nums:  # Check if list is empty
        return None  # Skipped (list is not empty)

    minimum = nums[0]  #  minimum = 7 (first element at index 0)

    for num in nums[1:]:  # nums[1:] creates a slice: [4, 3, 100, 2343243, 343434, 1, 2, 32]
        # Starts from index 1 (skips the first element 7)

        if num < minimum:
            minimum = num

    return minimum