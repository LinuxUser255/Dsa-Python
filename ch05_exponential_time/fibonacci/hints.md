# Hints: Fibonacci

## Hint 1: get it correct before you make it fast

Write the naive recursive version straight from the definition in `assignment.md`, and run the tests.
Which cases pass? Which time out? Write down the `Time:` for `n = 10`, `20` and `25`.
How much bigger does the time get for every +5?

## Hint 2: count the calls

Add a global counter that goes up by one each time `fib` is called.
How many calls does `fib(20)` make? `fib(25)`? Compare that with how many *different* values of `n`
there are below 25.

## Hint 3: build up, don't break down

The naive version starts at `n` and works *down*. Try going *up* instead:
start from `fib(0)` and `fib(1)` and walk forward to `n`.

On paper: if you know `fib(5) = 5` and `fib(6) = 8`, what's `fib(7)`?
And once you have `fib(7)`, do you still need `fib(5)`?

## Hint 4: how many variables?

If you only ever need the previous two numbers, how many variables do you need? (Not a list.)
At each step, both variables "slide forward" by one.
Python's tuple unpacking from the bubble sort swap is handy here: `a, b = ..., ...`.

## Hint 5: edge cases

Check `n = 0` and `n = 1` against your loop. Does your loop run zero times for them, and still
return the right thing? Or do they need an early `return`?

## Hint 6: the other way (memoization)

You can also keep the recursive shape and add a dictionary of answers you've already computed:
before computing `fib(k)`, check whether it's already stored.
Look up `functools.cache` too, but write the dictionary version yourself first.

## Self-check

- Only the large-`n` cases fail on time? You're still recomputing subproblems.
- Off by one position (for example `fib(10)` gives `34` or `89`)? Check how many times your loop runs.
