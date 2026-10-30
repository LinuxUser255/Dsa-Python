# Hints: Count Job Titles

## Hint 1: unpack the tuples

Each user is a 2-item tuple. You can unpack it right in the `for` line, so you get two named variables
instead of writing `user[1]`. Which of the two do you actually need?

## Hint 2: the first time vs every other time

The first time you see `"Engineer"`, it's not in the dict yet, so `counts["Engineer"] += 1` raises a
`KeyError`. Every time after that, it's there.
How can you tell which situation you're in? (Look at the O(1) operations table in `assignment.md`.)

## Hint 3: a shortcut

`d.get(key, default)` returns `default` instead of crashing when `key` is missing.
How could that turn the two cases from Hint 2 into one line?

## Hint 4: don't count with `list.count`

You *could* collect all the titles, then call `titles.count(title)` for each distinct one.
That works, but each `.count()` scans the whole list again. With `k` distinct titles that's O(n × k),
instead of one O(n) pass.

## Self-check

- `KeyError: 'Engineer'`? Re-read Hint 2.
- Counts are all 1? You're *setting* the count instead of *adding* to it.
