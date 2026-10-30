#!/usr/bin/env python3
"""
A quick tour of list, tuple, dict and set behaviour that trips people up.
"""


def section(title):
    print(f"\n=== {title} ===")


def main():
    section("1. Tuples are immutable")
    record = (7, "ana", "Engineer")
    try:
        record[2] = "Manager"  # type: ignore  # deliberate: this is the error being demonstrated
    except TypeError as e:
        print(f"record[2] = 'Manager' -> TypeError: {e}")
    updated = record[:2] + ("Manager",)
    print(f"make a new tuple instead: {updated}")

    section("2. Only hashable (immutable) things can be dict keys / set items")
    locations = {(40.7, -74.0): "New York"}  # a tuple key is fine
    print(f"tuple key works: {locations}")
    try:
        {["python", "sql"]: "skills"}  # type: ignore  # deliberate: this is the error being demonstrated
    except TypeError as e:
        print(f"list as a key -> TypeError: {e}")

    section("3. Sets have no order, and drop duplicates")
    tags = ["python", "sql", "python", "go", "sql"]
    print(f"list:          {tags}")
    print(f"set(list):     {set(tags)}   <- order not guaranteed!")
    print(f"sorted(set()): {sorted(set(tags))}")
    print(f"keep first-seen order AND drop duplicates: {list(dict.fromkeys(tags))}")

    section("4. {} is a dict, not a set")
    print(f"type({{}})     = {type({}).__name__}")
    print(f"type(set())  = {type(set()).__name__}")

    section("5. The shared-reference trap")
    grid = [[0] * 3] * 3  # three references to the SAME inner list
    grid[0][0] = 9
    print(f"[[0] * 3] * 3, then grid[0][0] = 9 -> {grid}")
    grid = [[0] * 3 for _ in range(3)]  # three separate lists
    grid[0][0] = 9
    print(f"[[0] * 3 for _ in range(3)], same change -> {grid}")

    section("6. Assignment doesn't copy")
    original = ["ana", "ben"]
    alias = original
    alias.append("cy")
    print(f"alias = original; alias.append('cy') -> original is now {original}")
    copy = list(original)
    copy.append("dee")
    print(f"copy = list(original); copy.append('dee') -> original still {original}")

    section("7. Dicts remember insertion order (Python 3.7+)")
    last_seen = {}
    last_seen["zed"] = "09:00"
    last_seen["amy"] = "09:05"
    last_seen["max"] = "09:10"
    last_seen["zed"] = "09:15"  # updating a key keeps its original position
    print(last_seen)


if __name__ == "__main__":
    main()
