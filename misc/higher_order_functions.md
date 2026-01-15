
```python

def transform_list(nums_list, transform_item):
    transform_item(nums_list[0])
    
my_list = [2, 3]

```
```python
# lambda refactor
def transform_list(nums_list, transform_item):
    """Apply transform_item to each element in nums_list and return new list."""
    # Fix: Use a loop or comprehension to make it general:
    return [transform_item(num) for num in nums_list]


# Example usage
print(transform_list([2, 3, 4], lambda num: num ** 2))  # [4, 9, 16]
print(transform_list([2, 3, 4], lambda num: num ** 3))  # [8, 27, 64]

```


Here's a concise higher-order function example using a **regular named function** (no lambda):

```python
# Higher-order function: accepts a function as argument
def apply_operation(numbers, operation):
    result = []
    for num in numbers:
        result.append(operation(num))  # Call the passed-in function
    return result
```
```python
# lambda refactor
def transform_list(nums_list, transform_item):
    """Apply transform_item to each element in nums_list and return new list."""
    # Fix: Use a loop or comprehension to make it general:
    return [transform_item(num) for num in nums_list]


# Example usage
print(transform_list([2, 3, 4], lambda num: num ** 2))  # [4, 9, 16]
print(transform_list([2, 3, 4], lambda num: num ** 3))  # [8, 27, 64]

```



```python
# Normal functions to pass in
def square(x):
    return x ** 2

def double(x):
    return x * 2

# Usage
nums = [1, 2, 3, 4, 5]

print(apply_operation(nums, square))  # [1, 4, 9, 16, 25]
print(apply_operation(nums, double))  # [2, 4, 6, 8, 10]
```

**Explanation**:
- `apply_operation` is a **higher-order function** because it takes another function (`operation`) as a parameter.
- `square` and `double` are normal, named functions.
- You can pass either one to `apply_operation`, making it reusable and flexible.

Clean, readable, and a classic example of higher-order functions in Python! 😊