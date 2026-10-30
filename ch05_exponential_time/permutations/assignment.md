# Permutations: O(n!), Worse Than Exponential

A **permutation** is one possible *ordering* of a collection. Unlike the power set, every item is
always included; only the order changes.

```
speakers:  ["ana", "ben", "cy"]
orderings: ana ben cy | ana cy ben | ben ana cy | ben cy ana | cy ana ben | cy ben ana
```

How many are there? There are `n` choices for the first slot, `n - 1` for the second, `n - 2` for the
third, and so on: `n × (n-1) × ... × 1` = **n!** (factorial, from Chapter 2).

| n  | 2ⁿ        | n!         |
|----|-----------|------------|
| 5  | 32        | 120        |
| 10 | 1,024     | 3,628,800  |
| 15 | 32,768    | 1,307,674,368,000 |
| 20 | 1,048,576 | 2,432,902,008,176,640,000 |

Factorial growth leaves even 2ⁿ behind. This is why the famous *travelling salesman* problem can't be
brute-forced: just 20 cities can be visited in 20! orders, about 2.4 quintillion.
(Removing round trips that are the same loop with a different start or direction still leaves about 60 quadrillion.)

## Assignment

LockedIn is hosting a conference, and the organisers want to review **every possible speaker lineup**.
Complete `get_orderings(speakers)`.

- It takes a list of **unique** speaker names.
- It returns a list of lists: every ordering, each exactly once.
- The order *of* the orderings doesn't matter, but the order **inside** each ordering does (that's the
  whole point).
- The orderings of an empty list is `[[]]`: exactly one way to arrange nothing (0! = 1).
- Don't use `itertools.permutations`.

### The recursive idea

Pick who speaks **first**. Then the rest of the lineup is just *every ordering of everyone else*,
which is the same problem, one speaker smaller.

1. **Base case:** if there are no speakers, return `[[]]`.
2. For each speaker `s` in the list:
   1. Make a list of the *other* speakers (everyone except `s`).
   2. Recursively get every ordering of the others.
   3. Put `s` at the front of each of those orderings and add them to your result.
3. Return the result.

The last test uses 7 speakers: 5,040 lineups. Try 10 in a REPL (3.6 million) and see how much longer it takes.
