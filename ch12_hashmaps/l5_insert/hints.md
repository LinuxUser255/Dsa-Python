# Hints: `HashMap.insert`

Try one hint at a time, then go back to the code.

## Hint 1: read the test before the assignment

`assignment.md` talks about `self.buckets` and `self.size`. **Your `main.py` doesn't have either.**
Look at `__init__` in `main.py`: what is the list actually called?
Then look at `hashmap_to_list()` in `main_test.py`: which attribute does the test read?
Whatever name you write to has to be the name the test reads.

## Hint 2: you already have the hard part

Everything below `# don't touch below this line` is yours to *use*.
One of those methods already turns a string into a valid list position.
Should `insert` re-do that math, or ask for it?

## Hint 3: what does "stored" look like?

Open `main_test.py` and find the expected list in `run_cases`. What *shape* is each non-`None` slot?
Is it just the value? Just the key? Or something holding both?

## Hint 4: trace the run case by hand

`run_cases` uses a size-4 map and two users: `Dave#3` and `Shelley#2`.

1. Sum the `ord()` of each character in `"Dave#3"`, then `% 4`. Does it land on index 2?
2. Do the same for `"Shelley#2"`. Does it land on index 3?

If your hand-trace matches the expected list, you know exactly where each item belongs.

## Hint 5: what should `insert` return?

Check the test again: does it use the return value of `hm.insert(...)` at all?
What does that tell you about where the result needs to end up?

## Self-check

- Run `python main_test.py` from this folder (or `pytest ch12_hashmaps/l5_insert` from the repo root).
- If you see `Error: 'HashMap' object has no attribute ...`, re-read Hint 1.
- If every slot prints `None`, your method isn't saving anything onto `self`.
