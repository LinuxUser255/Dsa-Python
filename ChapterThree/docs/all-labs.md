# All labs from  Big O Notation


## L2: O(n) - Order “n”
O(n) is very common - When the number of steps in an algorithm grows at the same rate as its input size, it's classified as O(n)

For example, our find min algorithm from earlier is O(n):

Set min to positive infinity.
For each number in the list, compare it to min. If it is smaller, set min to that number.
min is now set to the smallest number in the list.
The input to the find min algorithm is a list of size n. Because we loop over each item in the input once, we add one step to our algorithm for each item in our list.

As we use find min with larger and larger inputs, the length of time it takes to execute the function grows at a steady linear pace. We can reasonably estimate the time it will take to run, based on a previous measurement. If we find that:

Input size	Time to run
find_min(10 items)	2 ms
Then we can estimate the following:

Input size	Time to run
find_min(100 items)	20 ms
find_min(1000 items)	200 ms
find_min(10000 items)	2000 ms
Assignment
LockedIn users want to know which of their followers has the highest engagement score.

Complete the find_max function. It should take a list of integers and return the largest value in the list.

The "runtime complexity" (aka Big O) of this function should be O(n)



- Solution
```python
def find_max(nums):
    """take a list of integers and returns the maximum value"""

    if not nums:  # Check if list is empty
        return None  # Skipped (list is not empty)

    max_value = nums[0]  # Initialize max_value with first element in nums

    for num in nums[1:]:  # nums[1:] creates a slice: [4, 3, 100, 2343243, 343434, 1, 2, 32]
        if num > max_value:
            max_value = num

    return max_value
```

## L3: O(n^2) - Order “N Squared”

O(n^2) grows in complexity much more rapidly. That said, for small and medium input sizes, these algorithms can still be very useful.

A common reason an algorithm falls into O(n^2) is by using a nested loop, where the number of iterations of each loop is equal to the number of items in the input:

```python
for person_one in persons:
    for person_two in persons:
        # every combination of people
        # will go on a date... twice!
        go_on_date(person_one, person_two)
```

Assignment
LockedIn needs search capabilities! For now, we'll build something slow (and frankly awful) so we can see an n^2 algorithm in practice.

Complete the does_name_exist function.

For each first name in first_names:
For each last name in last_names:
If a first/last name combination (joined with a space) matches the full_name, it should return True.
If the loop finishes, it should return False.
Observe
When you run your completed code, notice how each successive call to does_name_exist takes quite a bit longer. Assuming the length of first_names and last_names is the same, each new name doesn't add n steps to the algorithm; the total number of steps grows quadratically with the size of the input, making the total work O(n^2).

If does_name_exist(10 names, 10 names) takes just 1 second to complete, then we can estimate:

does_name_exist(100 names, 100 names) = 100 seconds
does_name_exist(1000 names, 1000 names) = 10,000 seconds
does_name_exist(10000 names, 10000 names) = 1,000,000 seconds


- Solution
```python
def does_name_exist(first_names, last_names, full_name):
    for first in first_names:
        for last in last_names:
            try:
                if first + " " + last == full_name:
                    return True
            except Exception as e:
                print(f"An Error occurred while checking the name: {e}")
    return False
```

## N^2 Quiz

Refer to the following functions, and assume that first_names and last_names are the same length.

```python

def print_names_one(first_names):
    for first_name in first_names:
        print(first_name)

def print_names_two(first_names, last_names):
    for first_name in first_names:
        for last_name in last_names:
            print(first_name, last_name)
```


What are the Big O complexities of print_names_one and print_names_two respectively?

_O(n), O(n^2)_

Which function will finish faster, assuming first_names and last_names are the same non-zero length?
`_print_names_one_`

## L6: O(nm)

O(nm) is very similar to O(n^2), but instead of a single input that we care about, there are two. If n and m increase at the same rate, then O(nm) is effectively the same as O(n^2). However, if n or m increases faster or slower, then it's useful to track their complexity separately.

#### Assignment
LockedIn needs a new tool that allows big brands to see how many of an influencer's followers are loyal to their brand. Complete the get_avg_brand_followers function. It takes two inputs:

all_handles: a 2-dimensional list, or "list of lists" of strings representing user handles on a per-influencer basis.
brand_name: a string.
get_avg_brand_followers returns the average number of handles that contain the brand_name across all the lists. Each list represents the audience of a single influencer.

Example Input/Output
Input:
```python
all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
]
brand_name = "cosmo"
```

Expected output: 1.33 (handles per influencer, because 4 handles contained "cosmo" and there are 3 lists)

#### Observe
Regarding Big O, the number of influencers (the number of lists) matters. That's our n. However, the average number of followers of each influencer (the average length of the lists) is just as important. That's our m.

- Solution
```python
def get_avg_brand_followers(all_handles, brand_name):
    # 2. Initialize Counters
    total_matching = 0 # count all handles containing the brand
    num_influencers = len(all_handles) # `n` length of all_handles

    for handles in all_handles: # loop over each influencer `n`
        for handle in handles: # handles of the current influencer `m
            try:
                if brand_name in handle:
                    total_matching += 1 # increment the counter
            except Exception as e:
                print(f'''An Error occurred
                 while matching brand names to handles: {e}''')
            else:
                # if no exception was raised, continue to next handle
                continue
    # 5. Calculate and return the average
    if num_influencers == 0:
        return 0
    else:
        return total_matching / num_influencers # as float

```


## L7: Constants Don't Matter

a)

Big-O notation only describes the theoretical growth rate of algorithms. 
It doesn't deal with the actual time an algorithm takes to run on a given machine. 
As such, when doing Big O analysis, we don't let ourselves get bogged down in details.

For example, take a look at the following functions:

```python

def print_names_once(names):
    for name in names:
        print(name)

def print_names_twice(names):
    for name in names:
        print(name)
    for name in names:
        print(name)

```

As you would expect, print_names_once will take half the time to run as print_names_twice. And in the real world of
software engineering, cutting speed in half is awesome. The funny thing about Big O analysis is that we don't care.
We're academics™.

Both of the functions above have the same rate of growth, O(n). You might be tempted to say, "print_names_twice should
be O(2 * n)" but you would be missing the whole point of Big O.

In Big O analysis we drop all constants because while they affect the runtime, they don't affect the change in the
runtime.

O(2 * n) -> O(n)
O(10 * n^2) -> O(n^2)

_O(2^n)_


## L8: Constants Don't Matter

### How would we reduce `O(2 * log(2 * n))?`

### `O(log(n))`



## L9: Constants Quiz 

### Contants Quiz

Consider the following functions:
```python
def sum(nums):
    total = 0
    for num in nums:
        total+=num
    return total
```

```python
def double_sum(nums):
    total = 0
    for num in nums:
        double = num + num
        total += double
    return total
```

### What is the Big O of `sum()` and `double_sum()` respectively?

### `O(n) O(n)`



## L10: Constants Quiz

Consider the following functions:
```python
def sum(nums):
    total = 0
    for num in nums:
        total+=num
    return total
```

```python
def double_sum(nums):
    total = 0
    for num in nums:
        double = num + num
        total += double
    return total
```
Ignoring Big-O theory, which function will realistically take longer to execute?

`double_sum`

## L11: Order 1
O(1) means that no matter the size of the input, there is no growth in the runtime of the algorithm. This is also referred to as a "constant time" algorithm.

In Python, a dictionary offers the ability to look items up by key, which is an operation that is independent of the size of the dictionary:

```python
# this is a constant time lookup
org = organizations[org_id]
```

Dictionary lookups are O(1). Which is one of the reasons dictionaries and dictionary-equivalents in other languages are used all over the place.

Assignment
We need to be able to search our LockedIn user base more quickly! Our users are complaining that the search bar is painfully slow. You'll notice that if you run the code in its current state, it will take a very long time.

The find_last_name function takes

names_dict: a dictionary of first_name -> last_name.
first_name: a string.
If first_name is a key in the dictionary, find_last_name returns the associated last name. If the key is not found, it returns None.

Write the function so that it runs quickly! It should be O(1).

```python
def find_last_name(names_dict, first_name):
    return names_dict.get(first_name)
```

## L12: Order Log N
O(log(n)) algorithms are only slightly slower than O(1), but much faster than O(n). They do grow according to the input size, n, but only according to the log of the input.

O(n):

n	time
8	8 ms
64	64 ms
1024	1024 ms
1048576	1048576 ms
O(log(n)):

n	time
8	3 ms
64	6 ms
1024	10 ms
1048576	20 ms
Binary Search

A binary search algorithm is a common example of an O(log(n)) algorithm. Binary searches work on a pre-sorted list of elements.

Pseudocode
Given two inputs:

A list of n elements sorted from least to greatest
A target value:
Do the following:

Set low = 0 and high = n - 1.
While low <= high:
Set median (the position of the middle element) to (low + high) // 2, which is the greatest integer less than or equal to (low + high) / 2
If list[median] == target, return True
Else if list[median] < target, set low to median + 1
Otherwise set high to median - 1
Return False
At each iteration of loop, we halve the list. Which makes the algorithm O(log(n)). In other words, to add one more step to the runtime, we'd have to double the size of the input. Binary searches are fast.

Assignment
We have a popular influencer using our LockedIn app, and she needs to be able to quickly search for posts from a particular day. This function will be the backbone of her search screen.

Complete the binary_search function. It should follow the algorithm as described above.

```python
def binary_search(target, arr):
    """
    Perform binary search on a sorted array.

    Time Complexity: O(log n) - efficiently handles large arrays (e.g., 2M elements in <50ms)
    Space Complexity: O(1) - iterative approach with constant space

    Args:
        target: The value to search for
        arr: A sorted list in ascending order

    Returns:
        bool: True if target is found, False otherwise

    Note:
        - Assumes arr is pre-sorted in ascending order
        - Handles edge cases: empty array, single element, missing target
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate middle index using integer division
        # Avoids potential overflow: mid = low + (high - low) // 2
        mid = (low + high) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return False
```

## L13: Name Count

In LockedIn, we process tons of users' names. They are often structured as lists of lists. For example, a separate list of users for each influencer's followers.

Assignment
Complete the count_names function.

It should iterate over all the names in the nested list_of_lists and count all the instances of target_name, then return the count.

Observe
What's the time complexity of your solution? It should be O(n) on the total number of names, but O(mn) if you consider m to be the number of lists and n to be the average length of a list.

```python
def count_names(list_of_lists, target_name):
    """
    Core task: Traverse a nested list structure to count all occurrences of a specific `target_name`

        Count how many times `target_name` appears across all names in a nested list of lists.

        Args:
            `list_of_lists`: A list containing inner lists of strings (names)
            `target_name`: The name to count (str)

        Returns:
            int: The total count of `target_name` across all inner lists

        Time Complexity: O(n) where n is the total number of names
                         (or O(m * n) with m outer lists and n average inner length)

                         n = number of lists
                         m = average length of each list

        Space Complexity: O(1) - no extra space beyond a counter
        """
    # Step 1. Initialize a counter for the target name
    count = 0

    # Step 2. Iterate over each inner list
    for inner_list in list_of_lists:

        # Step 3. Iterate over each name in the inner list
        for name in inner_list:

            # Step 4. If the current name matches the target, increment the counter
            if name == target_name:
                count += 1

    return count
```


