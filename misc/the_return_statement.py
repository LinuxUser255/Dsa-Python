#!/usr/bin/env python3

unit = 'feet squared'


def calculate_area(length, width):
    area = length * width
    return area


# capture the return value in a variable,
# and set that variable to call the function
area = calculate_area(14, 10)

# the string value of unit is 'feet squared' and is passed to the print function
print(area, unit)
# output:
# 140 square feet squared
