# O(nm) Exercise: Average Brand Followers

## Objective
Implement the `get_avg_brand_followers()` function to calculate the average number of followers (per influencer) whose handle contains a given `brand_name`.

This demonstrates **O(nm)** time complexity, where:
- `n` = number of influencers (number of lists)
- `m` = average number of followers per influencer (average length of inner lists)

## Step-by-Step Implementation Instructions

1. **Define the function signature**  
   The function takes two parameters:
   - `all_handles`: a list of lists of strings (each inner list = one influencer's followers)
   - `brand_name`: a string to search for in handles

2. **Initialize counters**  
   - Create a variable `total_matching` = 0 (to count all handles containing the brand)
   - Create a variable `num_influencers` = length of `all_handles` (this is `n`)

3. **Loop over each influencer (outer loop – n times)**  
   - For each inner list in `all_handles`:

4. **Loop over each handle in the current influencer (inner loop – m times on average)**  
   - For each handle string:
     - Check if `brand_name` is in the handle (use `'in'` keyword: `brand_name in handle`)
     - If yes, increment `total_matching` by 1

5. **Calculate and return the average**  
   - If `num_influencers` is 0, return 0 (avoid division by zero)
   - Otherwise, return `total_matching / num_influencers` (as a float)

## Example Walkthrough
```python
all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],     # 2 matches
    ["cosmokiller", "gr8", "cosmojane3"],             # 2 matches
    ["iloveboots", "paperthin"]                       # 0 matches
]
brand_name = "cosmo"
```
- Total matches = 4
- Number of influencers = 3
- Average = 4 / 3 ≈ 1.333...

## Big O Observation
- Outer loop runs **n** times (one per influencer)
- Inner loop runs **m** times on average (followers per influencer)
- Total operations ≈ **n × m** → **O(nm)** complexity

If both n and m grow at the same rate, this behaves like O(n²). But tracking them separately is useful when one grows faster than the other.

Good luck — this nested loop will clearly show quadratic-like growth! 😊

---

# Hypothetical Real-life example of this..

### Hypothetical Analogy: O(nm) for "Shared Tesla Followers" on X

Imagine X wants a feature: **"How many of my followers are also Tesla fans?"**  
For a given user (you), the algorithm checks how many of **your followers** also follow **@Tesla**.

This maps perfectly to the O(nm) exercise.

#### Mapping the Variables
- **n** = number of your followers (the "influencers" in the exercise — each has their own list of followed accounts).
- **m** = average number of accounts each of your followers follows (the "audience size" — length of each inner list).
- **brand_name** = "Tesla" (the target we're searching for in handles/accounts).

#### Data Structure (like `all_handles`)
```python
all_followed_by_my_followers = [
    ["@elonmusk", "@Tesla", "@SpaceX"],           # Follower 1 follows these
    ["@Apple", "@Tesla", "@OpenAI"],              # Follower 2
    ["@Netflix", "@Disney", "@Amazon"],           # Follower 3 (no Tesla)
    # ... thousands more followers
]
brand_account = "Tesla"
```

#### The O(nm) Algorithm
To compute the **average number** of your followers who also follow Tesla:

1. Initialize `total_tesla_fans = 0`
2. For each of your **n followers** (outer loop):
   - Look at their list of followed accounts (average length **m**)
   - For each account in that list (inner loop):
     - If it contains "Tesla" → count +1
3. Average = `total_tesla_fans / n`

#### Why O(nm)?
- You examine **every followed account** of **every one of your followers**.
- Total operations ≈ **n × m**
- If you have 1,000 followers who each follow 500 accounts → ~500,000 checks → O(nm)

Just like the brand followers exercise: nested loops over two independent dimensions → quadratic in the product of their sizes.

Perfect analogy — same structure, same complexity! 😊