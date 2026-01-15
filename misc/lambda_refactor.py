#!/usr/bin/env python3

"""Using lambda to Eliminate need for a square and cube functions"""

#def square(num):
#    return num ** 2


#def cube(num):
#    return num ** 3

def transform_list(nums_list, transform_item):
    """Apply transform_item to each element in nums_list and return new list."""
    # Fix: Use a loop or comprehension to make it general:
    return [transform_item(num) for num in nums_list]


# Example usage
print(transform_list([2, 3, 4], lambda num: num ** 2))  # [4, 9, 16]
print(transform_list([2, 3, 4], lambda num: num ** 3))  # [8, 27, 64]

