#!/usr/bin/env python3

def bubble_sort(nums: list[int]) -> list[int]:
    follower_count = len(nums)
    swapping = True
    end = follower_count

    while swapping:
        swapping = False
        # [5, 7, 3, 6, 8]
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                # swap using Python's tuple unpacking
               temp = nums[i - 1]     # 1. save the value before it gets overwritten
               nums[i - 1] = nums[i]  # 2. overwrite the first slot
               nums[i] = temp         # 3. put the saved value in the second slot
               swapping = True

        end -= 1
    return nums

# nums[i-1], nums[i] = nums[i], nums[i-1] # pythonic way


