#!/usr/bin/env python3

# Regular function to square a number
# and
# lambda function to square a number
def square_n(num):
    return num ** 2


square = square_n(6)
print(square)  # Output: 36


sq = lambda num: num ** 2
print(sq(5)) # output: 25
