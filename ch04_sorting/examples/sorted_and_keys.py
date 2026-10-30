#!/usr/bin/env python3
"""
Sorting in practice with Python's built-ins.

Covers:
    1. sorted() vs list.sort()
    2. key= and reverse=
    3. sorting by more than one field
    4. why a *stable* sort matters
"""

# (name, job_title, followers)
users = [
    ("dave", "Engineer", 120),
    ("alice", "Designer", 950),
    ("carol", "Engineer", 950),
    ("bob", "Manager", 40),
    ("erin", "Designer", 300),
]


def show(title, rows):
    print(f"\n{title}")
    for row in rows:
        print(f"  {row}")


def main():
    # 1. sorted() returns a NEW list. The original is untouched.
    by_name = sorted(users)
    show("sorted(users): tuples compare field by field, so this sorts by name", by_name)
    show("users is unchanged", users)

    # list.sort() changes the list itself and returns None
    copy = list(users)
    returned = copy.sort()
    print(f"\ncopy.sort() returned {returned!r}  <- don't write `copy = copy.sort()`")

    # 2. key= tells sort WHAT to compare; reverse=True flips the order
    by_followers = sorted(users, key=lambda user: user[2], reverse=True)
    show("most followers first: key=lambda user: user[2], reverse=True", by_followers)

    # 3. Sort by several fields: return a tuple from key=
    #    job title A to Z, then followers high to low (negate a number to flip just that field)
    by_title_then_followers = sorted(users, key=lambda user: (user[1], -user[2]))
    show("by job title, then by followers (high to low)", by_title_then_followers)

    # 4. Stability: equal keys keep their existing order.
    #    Sort by name first, then by job title. Within each title, names stay A to Z
    #    because the second sort is stable.
    step_one = sorted(users, key=lambda user: user[0])
    step_two = sorted(step_one, key=lambda user: user[1])
    show("stable two-step sort: by name, then by title (names stay A to Z inside each title)", step_two)


if __name__ == "__main__":
    main()
