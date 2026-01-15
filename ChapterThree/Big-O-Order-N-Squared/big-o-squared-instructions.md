# O(n²) Exercise: Check if a Full Name Exists

## Objective
Implement the `does_name_exist()` function to check if a given `full_name` can be formed by combining one name from `first_names` and one from `last_names`.

```python
def does_name_exist(first_names, last_names, full_name):
    pass
```


This is intentionally inefficient to demonstrate **quadratic time complexity O(n²)**.

## Step-by-Step Implementation Instructions

1. **Define the function signature**  
   The function takes three parameters:
   - `first_names`: list of strings (first names)
   - `last_names`: list of strings (last names)
   - `full_name`: string to search for (e.g., "John Doe")

2. **Use nested loops**  
   - Outer loop: iterate over **each** name in `first_names`
   - Inner loop: iterate over **each** name in `last_names`

3. **Check each combination**  
   - Inside the inner loop, create the combined name: `first + " " + last`
   - Compare it to `full_name`
   - If they match, **immediately return `True`**

4. **Handle no match**  
   - If the nested loops complete without finding a match, **return `False`**

## Expected Behavior & Observation
- The function performs **n × n** comparisons (where n is the length of each list).
- Runtime grows **quadratically**:
  
  | Input Size (n names each) | Approximate Time     |
  |---------------------------|----------------------|
  | 10                        | ~1 second           |
  | 100                       | ~100 seconds        |
  | 1,000                     | ~10,000 seconds     |
  | 10,000                    | ~1,000,000 seconds  |

This dramatic slowdown illustrates why O(n²) algorithms become impractical for large inputs.

Good luck — embrace the slowness to truly feel the impact of quadratic growth! 😊