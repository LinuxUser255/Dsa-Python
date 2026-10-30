# Fibonacci: Escaping Exponential Time

The Fibonacci sequence starts `0, 1`, and every number after that is the sum of the two before it:

```
n:      0  1  2  3  4  5  6   7   8   9  10
fib(n): 0  1  1  2  3  5  8  13  21  34  55
```

The definition is recursive, so the "obvious" code is too:

```
fib(n) = n                        if n < 2
fib(n) = fib(n - 1) + fib(n - 2)  otherwise
```

That's correct, but **exponentially slow**. Draw the calls for `fib(5)`:

```
                      fib(5)
               /                \
          fib(4)                 fib(3)
         /      \               /      \
     fib(3)    fib(2)       fib(2)    fib(1)
     /   \     /   \        /   \
 fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
  /  \
fib(1) fib(0)
```

`fib(3)` is computed **twice** and `fib(2)` **three times**. Every call splits into two more calls, so
the tree roughly doubles with each level. The naive version is about **O(2ⁿ)**: `fib(32)` makes
over 7 million calls, and `fib(90)` would take longer than you'll live.

## Assignment

LockedIn's growth team models viral sharing with Fibonacci numbers, and they need large values fast.
Complete `fib(n)` in `main.py` so that:

- `fib(0) == 0`, `fib(1) == 1`, and `fib(n) == fib(n - 1) + fib(n - 2)` for larger `n`
- **every** test, including `fib(90)`, finishes in under **50 milliseconds**

**Suggested approach:**

1. First, write the naive recursive version above and run the tests. Watch the `Time:` lines. At which
   `n` does it fall over?
2. Then make it fast. Notice that to get the next Fibonacci number, you only ever need the **previous
   two**. You never need anything older.

Your final version should be **O(n)**.

## The lesson

The problem didn't change; only the algorithm did. Exponential time usually comes from **redoing
work you've already done**. Remembering answers ("memoization"), or building up from the bottom,
often turns exponential into polynomial.
That idea has a name, *dynamic programming*, and you'll see it again and again.
