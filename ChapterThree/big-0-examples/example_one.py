"""
Big O examples:

O(n) Linear proportional to the list size coming in.
O(1) Constant time regardless of the list size.
O(n^2) Quadratic proportional to the square of the list size coming in.
Binary search: O(log n) dividing the list in half each time.
O(log n) Logarithmic proportional to the list size coming in.
O(2^n) Exponential - Order 2 to the n times the list size.

The idea here is that the more numbers that are passed to the function,
the longer the time it will take to compute
"""

#def calc_product(nums):
#    if len(nums) == 0:
#        return 0
#
#    product = 1
#
#    for num in nums:
#        product *= num
#
#    return product
#
##print(calc_product(nums))
#
#def calc_list(nums = [5]):
#    if len([5]) == 0:
#        return 0
#
#    product = 1
#
#    for num in [5]:
#        product *= num
#
#    return product
#
##print(calc_list())  # Output: 5
#
#
#
#def calc_bigger_list(nums = [1,2,3,4,5]):
#    if len([1,2,3,4,5]) == 0:
#        return 0
#
#    product = 1
#
#    for num in [1,2,3,4,5]:
#        product *= num
#
#    return product
#
##print(calc_bigger_list())  # Output: 5

from functools import reduce


# Using List Comprehension & lambda implementation of `calc_product`
def calc_bigger_list(nums=[1, 2, 3, 4, 5]):
    """
    Define a lambda function to multiply two numbers x and y,
    using the `reduce()` function to multiply all elements in the list.
    """
    if len(nums) == 0:
        return 0

    # [1 * 2 * 3 * 4 * 5] = 120
    product = lambda x, y: x * y
    product = reduce(product, nums)

    return product


# call the function
print(calc_bigger_list())  # Output: 120
