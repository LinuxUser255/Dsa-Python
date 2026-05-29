**Here's me reading this new assignment to you clearly:**

---

**Assignment**

While the influencers who use our platform are really great at taking selfies, most aren't super great at math. We need to write a tool that predicts an influencer’s follower growth over time.

Complete the `get_follower_prediction` function. It takes a `follower_count` integer, an `influencer_type` string and a `num_months` integer, and returns an integer.

Calculate the number of followers an influencer will have after a given number of months according to the influencer type:

- "fitness": follower count quadruples each month  
- "cosmetic": follower count triples each month  
- other: follower count doubles each month  

For example, if a "fitness" influencer starts with 10 followers, then after 1 month they would have 40 followers. After 2 months, they would have 160 followers, and so on.

This kind of sequence, where each term is found by multiplying the previous term by a constant, is called a geometric sequence or geometric progression.

Use the following version of the geometric progression formula, in which `a1` is the initial number of followers, `r` is the multiplication constant, and `n` is the number of months:

```python
total = a1 × r^n
```

---

**Talking yourself through it**

Start by asking: *"What do I actually know going in?"*

- I have a starting follower count  
- I have an influencer type that determines how fast they grow  
- I have a number of months  

Then ask: *"What decision does my code need to make first?"*

The influencer type determines the multiplier `r`. So before any math happens, you need to figure out: is this fitness, cosmetic, or other? That's a branching decision — what structure do you use for that?

Then ask: *"Once I know the multiplier, what's the math?"*

You have the formula right there:

```python
total = a1 × r^n
```

Map that to your variable names:
- `a1` = ?
- `r` = ?
- `n` = ?

Then ask: *"What does the function need to return, and in what type?"*

The return type is `int` — but `**` with certain inputs can produce a float. So what might you need to do before returning?

---

Take a crack at stubbing out the structure before writing any math. What's the first thing you'd write?

---

## Proper thinking 
Great question, and worth stepping back for.

The core difference is this:

**Experts think in abstractions first, specifics second.**

Look at what the instructor wrote first:

```python
factor = 2
if influencer_type == "fitness":
    factor = 4
```

He didn't write the math yet. He didn't hardcode any numbers into a formula. He first asked *"what changes between cases?"* — and the answer is just the factor. So he isolated that into a variable, handled the decision, and *then* he'll apply the formula once at the end.

Now look at your first line:

```python
fitness_influencer = (4**2) * 10
```

You jumped straight to the math — with specific numbers plugged in. That's a natural instinct, because the example in the assignment uses concrete numbers. But the problem with hardcoding is that it only works for *one case*. The function needs to work for *any* follower count, *any* type, *any* number of months.

---

The paradigm shift is roughly this:

**Amateur:** *"Let me solve the example they gave me."*

**Expert:** *"Let me solve the general case, and the example will work automatically."*

The instructor's first move was to identify what *varies* — the factor — and represent it as a variable. Everything else flows from that.

So the internal monologue of an expert approaching this would sound like:

*"What are my inputs? What changes based on those inputs? What stays the same? Can I isolate the moving part first, then write the formula once?"*

---

# My solution
```python
def get_follower_prediction(follower_count, influencer_type, num_months):
    """
    Predicts an influencer's follower count after a given number of months.

    Approach — isolate what changes, then apply the formula once:
        1. What varies?  the growth factor is determined by influencer_type
        2. What stays the same?  the formula: total = a1 * r ** n

    Formula:
        total = a1 * r ** n
        a1 = follower_count  (starting followers)
        r  = factor          (4=fitness, 3=cosmetic, 2=other)
        n  = num_months

    Example:
        fitness, 10 followers, 2 months:
        total = 10 * 4**2 = 10 * 16 = 160
    """
    # Break the Approach into it's separate parts.
    # First, what changes between cases? 
    # It's The growth factor that changes between cases
    # what is the factor?? The influencer category type is the factor.
    #  r  = factor  (4=fitness, 3=cosmetic, 2=other)
    # so you have 3 factors, fitness, cosmetic, and other
    # so define, or set the factor variable first
    # begin with the "other" type
    factor = 2
    if influencer_type == "fitness": # factor 4
        factor = 4
    elif influencer_type == "cosmetic": # factor 3
        factor = 3

    # next, implement the equation
    # follower_count =  # a1
    # factor = # r
    # num_months = # n
    # formula
    # a1 * r ** n
    get_follower_prediction = follower_count * (factor ** num_months)
    return get_follower_prediction 
```

# my solution - no comments
```python
def get_follower_prediction(follower_count, influencer_type, num_months):
    factor = 2
    if influencer_type == "fitness":
        factor = 4
    elif influencer_type == "cosmetic":
        factor = 3

    get_follower_prediction = follower_count * (factor ** num_months)
    return get_follower_prediction 
```

```python
# the instructor using the match expression:
# case-switch in bash
def get_follower_prediction(follower_count, influencer_type, num_months):
    factor = 2

    match influencer_type:
        # when the case is fitness, the factor is 4
        case "fitness":
            factor = 4
        case  "cosmetic":
            factor = 3
    return  follower_count * (factor ** num_months)

```

```python
# Solution provided
# downside, If the formula ever changed, you'd need to update three lines.
def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        return follower_count * (4**num_months)
    if influencer_type == "cosmetic":
        return follower_count * (3**num_months)
    return follower_count * (2**num_months)

```
