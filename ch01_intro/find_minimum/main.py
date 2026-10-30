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