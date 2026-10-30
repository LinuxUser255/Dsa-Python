# Power Set: O(2ⁿ)

The **power set** of a collection is the set of **all its subsets**, including the empty one and the
whole thing.

```
items:     ["python", "sql"]
power set: [[], ["python"], ["sql"], ["python", "sql"]]
```

Why is it exponential? For **each** item there are exactly two choices: it's **in** the subset, or
it's **out**. With `n` items that's `2 × 2 × ... × 2` = **2ⁿ** subsets.

| items | subsets |
|-------|---------|
| 3     | 8       |
| 10    | 1,024   |
| 20    | 1,048,576 |
| 40    | ~1.1 trillion |

No clever trick avoids this. If the problem asks you to *list every subset*, the output alone is 2ⁿ long.

## Assignment

LockedIn lets users pick which skills to feature on their profile. Marketing wants every possible
combination of skills, to A/B test which combos get the most profile views.
Complete `power_set(items)`.

- It takes a list of **unique** items.
- It returns a list of lists, **every** subset of `items`, each subset exactly once.
- Order doesn't matter: neither the order of the subsets, nor the order inside each subset.
  The test sorts everything before comparing.
- Don't use `itertools`.

### The recursive idea

Look at the subsets of `["python", "sql"]` from the point of view of the **first** item:

- the subsets **without** `"python"`: `[]`, `["sql"]`
- the subsets **with** `"python"`: `["python"]`, `["python", "sql"]`

Notice that the "without" group is exactly the power set of the *rest* of the list, `["sql"]`.
And the "with" group is that same power set with `"python"` added to every subset.

1. **Base case:** the power set of `[]` is `[[]]`. That's one subset: the empty one.
2. Otherwise, take the first item, and recursively get the power set of the rest.
3. The answer is every subset from step 2, plus every subset from step 2 with the first item added.

Once it passes, look at the `12` items case: 4,096 subsets. Try 20 or 25 items in a REPL and see how
fast it stops being fun.
