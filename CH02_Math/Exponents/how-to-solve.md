from numpy.ma.extras import averagefrom numpy.ma.extras import average
Break it down - understand what's being asked
---
Let's break it into three plain-English pieces.

**What is "spread"?**

It's an estimate of how far a post travels after the original author's followers see it and reshare it. Posts spread exponentially — meaning the more followers your followers have, the faster it explodes outward.

**Understanding the inputs**

Say you're the author. You have 4 followers:

```
audiences_followers = [2, 3, 2, 19]
```

- You have 4 followers (the length of the list)
- Each number in the list is *that follower's* own follower count
- So follower 1 has 2 followers, follower 2 has 3 followers, and so on

**The formula broken down**

```
estimated_spread = average_audience_followers * (num_followers ** 1.2)
```

In plain English, that's two parts multiplied together:

- `average_audience_followers` — the average of the list. From `[2, 3, 2, 19]` that's `(2+3+2+19) / 4 = 6.5`. How influential are your followers on average?
- `num_followers ** 1.2` — how many followers you have, raised to the power of 1.2. The `** 1.2` is what makes it *exponential* — it grows faster than a simple count.

**The edge case**

If `audiences_followers` is empty, you have no followers, so just return `0`. This prevents a divide-by-zero when calculating the average.

---

So to implement this you need three things: 
compute the average of the list, 
get the length of the list, 
then plug both into the formula. 

## Break it down into step-by-step
1. Get the number of followers — that's the length of `audiences_followers`
2. Handle the edge case — if the list is empty, return `0` immediately (also prevents divide-by-zero in step 3)
3. Calculate the average — sum up all the values in the list, then divide by the number of followers from step 1
4. Plug into the formula — multiply the average by `num_followers ** 1.2`
5. Return the result



Then pseudo code it
```python
def get_estimated_spread(audiences_followers: list[int]) -> float:
    """
    Estimates how far a post will spread based on the author's audience.
    Formula:
    estimated_spread = average_audience_followers * (num_followers ** 1.2)
    """
    # audiences_followers = [2, 3, 2, 19]
    # 1. how many followers does the author have
    num_followers = ???
    
    # 2. Handle the edge case - what if there are no followers?
    if ???:
        return ??
    
    # 3. What is the average follower count of the audience? 
    average = ??? / ???
    
    # 4. apply the formula
    estimated_spread = aaverage * (??? ** 1.2)
    
    # 5. Return the result
    retrun ???

```
---

```python
def get_estimated_spread(audiences_followers: list[int]) -> float:
    """
    Estimates how far a post will spread based on the author's audience.
   
    Formula:
    `estimated_spread = average_audience_followers * (num_followers ** 1.2)`
    
     Break it down into step-by-step
    1. Get the number of followers — that's the length of `audiences_followers`
    2. Handle the edge case — if the list is empty, return `0` immediately (also prevents divide-by-zero in step 3)
    3. Calculate the average — 
    sum up all the values in the list, 
    then divide by the number of followers from step 1
    4. Plug into the formula — multiply the average by `num_followers ** 1.2`
    5. Return the result
    """
    # For example:
    # average_audience_followers — the average of the list. 
    # From [2, 3, 2, 19] that’s (2 + 3 + 2 + 19) / 4 = 6.5.
    # 1. Calculate how many followers does the author have
    num_followers = sum(audiences_followers) #  audiences_followers is a parameter in the function 
    
    # 2. Handle the edge case - what if there are no followers?
    if sum(audiences_followers) == 0:
        return 0
    
    # 3. What is the average follower count of the audience? 
    # sum up all the values in the list, sum(list_values)
    # then divide by the number of followers from step 1
    average = num_followers / sum(audiences_followers)
    
    # 4. apply the formula
    # estimated_spread = average_audience_followers * (num_followers ** 1.2)
    estimated_spread =  average * (num_followers ** 1.2)

    # step 5: send it back
    return estimated_spread
```
---

```python

def get_estimated_spread(audiences_followers: list[int]) -> float:
    """
    Estimates how far a post will spread based on the author's audience.
   
    Formula:
    `estimated_spread = average_audience_followers * (num_followers ** 1.2)`
    
     Break it down into step-by-step
    1. Get the number of followers — that's the length of `audiences_followers`
    2. Handle the edge case — if the list is empty, return `0` immediately (also prevents divide-by-zero in step 3)
    3. Calculate the average — 
    sum up all the values in the list, 
    then divide by the number of followers from step 1
    4. Plug into the formula — multiply the average by `num_followers ** 1.2`
    5. Return the result
    """
    # For example:
    # average_audience_followers — the average of the list. 
    # From [2, 3, 2, 19] that’s (2 + 3 + 2 + 19) / 4 = 6.5.
    # 1. Calculate how many followers does the author have
    num_followers = len(audiences_followers) #  audiences_followers is a parameter in the function 
    
    # 2. Handle the edge case - what if there are no followers?
    if sum(audiences_followers) == 0:
        return 0
    
    # 3. What is the average follower count of the audience? 
    # sum up all the values in the list, sum(list_values)
    # then divide by the number of followers from step 1
    average = num_followers / sum(audiences_followers)
    
    # 4. apply the formula
    # estimated_spread = average_audience_followers * (num_followers ** 1.2)
    estimated_spread =  average * (num_followers ** 1.2)

    # step 5: send it back
    return estimated_spread
```
---

# corrected -- passes all tests

```python
def get_estimated_spread(audiences_followers: list[int]) -> float:
    """
    Estimates how far a post will spread based on the author's audience.
   
    Formula:
    `estimated_spread = average_audience_followers * (num_followers ** 1.2)`
    
     Break it down into step-by-step
    1. Get the number of followers — that's the length of `audiences_followers`
    2. Handle the edge case — if the list is empty, return `0` immediately (also prevents divide-by-zero in step 3)
    3. Calculate the average — 
    sum up all the values in the list, 
    then divide by the number of followers from step 1
    4. Plug into the formula — multiply the average by `num_followers ** 1.2`
    5. Return the result
    """
    # For example:
    # average_audience_followers — the average of the list. 
    # From [2, 3, 2, 19] that’s (2 + 3 + 2 + 19) / 4 = 6.5.
    # 1. Calculate how many followers does the author have
    num_followers = len(audiences_followers) 
    
    # 2. Handle the edge case - what if there are no followers?
    # what am I guarding against?
    # If the list is empty -- meaning no followers at all
    if num_followers == 0:
        return 0
    
    # 3. What is the average follower count of the audience? 
    # sum up all the values in the list, sum(list_values)
    # then divide by the number of followers from step 1
    # To get an average, what two things do I need, and do I have them in the right places?
    # average = total / count
    average = sum(audiences_followers) / num_followers 
    
    # 4. apply the formula
    # estimated_spread = average_audience_followers * (num_followers ** 1.2)
    estimated_spread =  average * (num_followers ** 1.2)

    # step 5: send it back
    return estimated_spread
    
```

---

# Cleaned up and explained

```python
def get_estimated_spread(audiences_followers: list[int]) -> float:
    """
    Estimates how far a post will spread based on the author's audience.

    Formula:
        estimated_spread = average_audience_followers * (num_followers ** 1.2)

    Args:
        audiences_followers: follower counts of each of the author's followers.
            e.g. [2, 3, 2, 19] means 4 followers with 2, 3, 2, and 19 followers of their own.

    Returns:
        float: estimated spread. Returns 0 if the list is empty.
    """
    # Step 1: total number of followers = length of the list
    num_followers = len(audiences_followers)

    # Step 2: edge case — empty list means no followers, and avoids divide-by-zero in step 3
    if num_followers == 0:
        return 0

    # Step 3: average = total / count
    average = sum(audiences_followers) / num_followers

    # Step 4: apply the formula — the ** 1.2 exponent is what makes spread grow exponentially
    estimated_spread = average * (num_followers ** 1.2)

    return estimated_spread
```

---

# Provided Solution

broken down into smaller separate steps for understanding the underlying process

```python
def get_estimated_spread(audiences_followers: list[int]) -> float:
    """
    Estimates how far a post will spread based on the author's audience.

    Formula:
        estimated_spread = average_audience_followers * (num_followers ** 1.2)

    The exponent 1.2 models exponential growth — doubling followers
    more than doubles the spread, reflecting how resharing works in practice.

    Args:
        audiences_followers (list[int]): each value is the follower count
            of one of the author's followers.
            e.g. [2, 3, 2, 19] = 4 followers, with 2, 3, 2, 19 followers of their own.

    Returns:
        float: the estimated spread. Returns 0 if the list is empty.
    """
    # Step 1: count how many followers the author has
    num_followers = len(audiences_followers)

    # Step 2: guard against empty list — no followers means no spread,
    # and also prevents divide-by-zero when calculating the average
    if num_followers == 0:
        return 0

    # Step 3: manually sum all follower counts in the list
    # (same as sum() built-in, but written out to show the underlying loop)
    total = 0
    for num in audiences_followers:
        total += num

    # Step 4: average = total followers / number of followers
    average_audience_followers = total / num_followers

    # Step 5: apply the spread formula and return the result
    return average_audience_followers * (num_followers ** 1.2)

```




## Yes, raised to the power of 1.2, a decimal exponet

Yes, exactly. `num_followers ** 1.2` means "num_followers raised to the power of 1.2."

In Python `**` is the exponent operator. So:

- `2 ** 2` = 4 (2 raised to the power of 2)
- `2 ** 3` = 8 (2 raised to the power of 3)
- `2 ** 1.2` = 2.297... (2 raised to the power of 1.2)

The decimal exponent is what makes it grow *faster than linear but slower than quadratic*. Compare how these grow as followers increase:

```
followers    linear (x1)    x**1.2
10           10             15.8
100          100            251.1
1000         1000           3981.0
10000        10000          63095.7
```

So doubling your followers more than doubles your spread — that's the "exponential" nature of viral posts. The 1.2 was chosen by whoever designed the formula to model how social media sharing actually behaves in the real world.