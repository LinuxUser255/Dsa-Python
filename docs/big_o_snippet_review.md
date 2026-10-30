# Big-O Snippet Review

For this prompt, focus on how the number of operations grows as the input size grows.

Quick hints
A fixed number of steps usually suggests O(1)
One loop over the input often suggests O(n)
A loop inside another loop over the same input often suggests O(n^2)
Nested loops over different inputs often suggest O(nm)
Repeatedly cutting the problem in half often suggests O(log n)

## Snippets
```python
# a
def first_item(items):
    if len(items) == 0:
        return None
    return items[0]
```

```python
# b
def print_all(items):
    for item in items:
        print(item)
```

```python
# b
def print_all(items):
    for item in items:
        print(item)
```


```python
# d
def combine(names, scores):
    for name in names:
        for score in scores:
            print(name, score)
```

```python
# e
def halve_until_small(n):
    while n > 1:
        n = n // 2
        print(n)
```

