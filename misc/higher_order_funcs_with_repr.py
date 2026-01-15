# using __repr__()__ method defined inside the namespace.

def square(num):
    return num ** 2


def cube(num):
    return num ** 3


def transform_list(nums_list, transform_item):
    # assign transform to variable for efficiency
    transformed_0 = transform_item(nums_list[0])
    transformed_1 = transform_item(nums_list[1])
    return [transformed_0, transformed_1]


my_list = [2, 3]

# Calling the `transform_list():` function
# with square as the `transform_item` argument
transformed_list = transform_list(my_list, square)


#  __repr__() method in the transform_list function
def __repr__(self):
    return str(self)


# print the transformed list
print(transformed_list)  # Output: [4, 9]
