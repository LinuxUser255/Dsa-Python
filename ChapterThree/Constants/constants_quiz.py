import time


def single_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total


def double_sum(nums):
    total = 0
    for num in nums:
        double = num + num
        total += double
    return total


# Larger input to make differences measurable
nums = list(range(1_000_000))  # 1 million numbers


def compare_funcs(func1, func2, data, trials=5):
    time1 = timeit.timeit(lambda: func1(data), number=trials) / trials
    time2 = timeit.timeit(lambda: func2(data), number=trials) / trials
    print(f"{func1.__name__}: {time1:.6f}s")
    print(f"{func2.__name__}: {time2:.6f}s")


import timeit

compare_funcs(single_sum, double_sum, list(range(1_000_000)))

# Time single_sum
#start = time.time()
#single_sum(nums)
#end = time.time()
#print(f"single_sum time: {end - start:.6f} seconds")
#
## Time double_sum
#start = time.time()
#double_sum(nums)
#end = time.time()
#print(f"double_sum time: {end - start:.6f} seconds")


# super cool proper comparison function


# Output:

#"""
#Question:
#
#What is the Big O of sum() and double_sum()
#respectively?
#
#Both are
#"""
#
#def sum(nums):
#    total = 0
#    for num in nums:
#        total += num
#    return total
#
#print(sum([1, 2, 3, 4, 5]))  # Output: 15
#
#
#def double_sum(nums):
#    total = 0
#    for num in nums:
#        double = num + num # Double the current number
#        total += double # Add the doubled number to the total
#    return total
#
#
#print(double_sum([1, 2, 3, 4, 5]))  # Output: 30
