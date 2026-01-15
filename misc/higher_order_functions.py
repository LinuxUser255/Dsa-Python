#!/usr/bin/env python3

def square(num):
    return num ** 2


def cube(num):
    return num ** 3


def transform_list(nums_list, transform_item):
    """assign transform to variable for efficiency"""
    transformed_0 = transform_item(nums_list[0])
    transformed_1 = transform_item(nums_list[1])
    return [transformed_0, transformed_1]


my_list = [2, 3]
transformed_list = transform_list(my_list, square)

# print(transformed_list)  # Output: [4, 9]

# Print the transformed list using __repr__() method
# here it is defined in the outside namespace
# the __repr__() method is called on the transformed_list object
print(transformed_list.__repr__())