# Hints: Build a User Index

## Hint 1: what's the key, and what's the value?

You'll be *asked* for users by id. So what should the dict's **keys** be?
And the test wants the whole tuple back. So what should each **value** be?

## Hint 2: building the index

One loop over `users`, one dict assignment per user. Which part of each tuple goes in the `[...]`?
(Tuple unpacking in the `for` line works here, but remember you still need the *whole* tuple as the value.)

## Hint 3: missing ids

`index[99]` raises `KeyError` when 99 isn't there. You met a dict method in `job_title_counts` that
returns a default instead of crashing. What should the default be here?

## Hint 4: keep the order

The result must line up with `ids`: first answer for the first id, and so on.
Should you loop over `ids`, or over the index?

## Hint 5: don't search inside `get_users_by_ids`

If you see `for user in index.values()`, or anything like it inside the lookup loop, you've rebuilt an
O(n) search. Each id should cost one dict access, nothing more.

## Self-check

- `KeyError`? Re-read Hint 3.
- Right users, wrong order? Re-read Hint 4.
- Times out only on the 300,000-user case? Re-read Hint 5.
- Getting `"ana"` instead of `(7, "ana", "Engineer")`? Store the whole tuple as the value.
