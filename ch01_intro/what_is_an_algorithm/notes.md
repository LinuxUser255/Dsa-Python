# Algorithm Analysis — String Reversal

---

## What Is an Algorithm?

An **algorithm** is a finite, unambiguous sequence of steps to solve a problem.
Think of it like a recipe — the same ingredients + the same steps = the same result, every time.

This code qualifies as an algorithm because it:
- Has a clear **start and end**
- Follows **deterministic steps** (same input always gives same output)
- Solves a defined **computational problem** (reverse a string)
- Has **measurable efficiency** (we can calculate how long it takes)

---

## The Problem

> Given a string like `"foo bar"`, return it reversed: `"rab oof"`

---

## The Plan (Pseudocode)

Before writing code, it helps to sketch the steps in plain English:

```
1. Start with an input string          →  "foo bar"
2. Create an empty list to accumulate  →  []
3. Walk through the string backwards,
   adding each character to the list   →  ['r', 'a', 'b', ' ', 'o', 'o', 'f']
4. Join the list into a single string  →  "rab oof"
5. Return the result
```

---

## The Code

```python
def reverse_string(original: str) -> str:
    """
    Reverses a string one character at a time.

    Args:
        original: The string you want to reverse.

    Returns:
        A new string with the characters in reverse order.
    """
    reversed_chars = []              # Empty list — we'll fill this backwards

    for char in reversed(original):  # Walk through the string back-to-front
        reversed_chars.append(char)  # Add each character to our list

    return ''.join(reversed_chars)   # Glue the list back into one string
```

---

## Execution Walkthrough

Using `"foo bar"` as the input:

| Step | Action | State of `reversed_chars` |
|------|--------|--------------------------|
| 1 | Start | `[]` |
| 2 | Append `'r'` | `['r']` |
| 3 | Append `'a'` | `['r', 'a']` |
| 4 | Append `'b'` | `['r', 'a', 'b']` |
| 5 | Append `' '` | `['r', 'a', 'b', ' ']` |
| 6 | Append `'o'` | `['r', 'a', 'b', ' ', 'o']` |
| 7 | Append `'o'` | `['r', 'a', 'b', ' ', 'o', 'o']` |
| 8 | Append `'f'` | `['r', 'a', 'b', ' ', 'o', 'o', 'f']` |
| 9 | `''.join(...)` | `"rab oof"` ✅ |

---

## Why a List Instead of a String?

You might wonder: why not just build up a string directly, like `result += char`?

**Strings in Python are immutable** — once created, they can't be changed.
Every time you do `result += char`, Python secretly creates a *brand new string* behind
the scenes and throws the old one away. For a 1,000-character string, that's 1,000
throw-away strings created.

A list doesn't have this problem — appending to a list is fast and cheap.
Join it into a string once at the very end.

```python
# Slow (creates a new string on every iteration)
result = ""
for char in reversed(original):
    result += char          # O(n) work per step → O(n²) total

# Fast (one join at the end)
chars = []
for char in reversed(original):
    chars.append(char)      # O(1) work per step → O(n) total
return ''.join(chars)
```

---

## Efficiency (Big-O)

| Measure | This Algorithm | Why |
|---------|---------------|-----|
| **Time** | `O(n)` | We visit each character exactly once |
| **Space** | `O(n)` | We store all characters in a list |

`n` = the number of characters in the input string.
This is called **linear time** — double the input, double the work. That's good!

---

## A Note on Variables and References

A common point of confusion for beginners is the difference between
**copying a value** and **referencing the same object**.

```python
s = "foo bar"
input_str = s           # input_str points to the SAME string as s
input_str = list(s)     # NOW input_str points to a NEW list object
```

After the first line, both `s` and `input_str` refer to the **exact same string in memory** —
no copy is made. After the second line, `input_str` is reassigned to a brand new list,
while `s` is left completely untouched.

You can verify this yourself:

```python
s = "foo bar"
input_str = s
print(s is input_str)      # True  — same object in memory

input_str = list(s)
print(s is input_str)      # False — now they are different objects
print(type(s))             # <class 'str'>
print(type(input_str))     # <class 'list'>
```

**Practical takeaway:** the intermediate assignment `input_str = s` is redundant.
You can skip straight to `input_str = list(s)`, or skip the conversion entirely
since `reversed()` works directly on strings.

---

## Algorithmic Patterns Used Here

| Pattern | What It Looks Like |
|---------|--------------------|
| **Accumulation** | `reversed_chars = []` starts empty and grows each iteration |
| **Iteration** | `for char in reversed(original)` visits each element once |
| **Data Structure Selection** | List for fast appending; join once at the end |
| **Pipeline** | `reversed()` → `append()` → `join()` — each step feeds the next |

---

## Connection to Later DSA Topics

This short example quietly touches several bigger ideas you'll see again:

**Chapter 3 — Big-O Notation**
Linear `O(n)` time complexity, demonstrated concretely.

**Chapter 7 — Stacks**
Reversal is a classic **LIFO** (Last-In, First-Out) operation.
A stack version of this algorithm looks like:

```python
def reverse_with_stack(original: str) -> str:
    stack = list(original)  # Push all characters onto a stack
    result = []

    while stack:
        result.append(stack.pop())  # Pop from the top (LIFO)

    return ''.join(result)
```

The loop-based version and the stack version produce identical output —
they're two different implementations of the same algorithm.

**Palindrome Checks**
To check if a word reads the same forwards and backwards,
you reverse it and compare:

```python
def is_palindrome(word: str) -> bool:
    return word == ''.join(reversed(word))
```

---

## Test Cases to Try

```python
print(reverse_string("foo bar"))   # "rab oof"
print(reverse_string(""))          # ""       ← empty string
print(reverse_string("a"))         # "a"      ← single character
print(reverse_string("racecar"))   # "racecar" ← palindrome!
print(reverse_string("hi!@#"))     # "#@!ih"  ← special characters
```

---

## Key Takeaways

1. An algorithm is just a **repeatable, step-by-step process** for solving a problem.
2. **Lists are mutable; strings are not** — append to a list, join at the end.
3. Variable assignment creates a **reference**, not a copy.
4. Simple examples like this are the building blocks for everything else in DSA.