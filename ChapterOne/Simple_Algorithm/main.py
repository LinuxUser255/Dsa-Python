"""
ChapterOne/Simple_Algorithm/main.py
Goal
Create a function that takes a list of integers (`nums`) and
returns the sum of all elements. It must handle:

# Normal for loop
def summed(nums):
    total = 0
    for number in nums:
        total += number

    return total
"""
# List comprehension
def summed(nums):
    return sum(num for num in nums)
