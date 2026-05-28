#!/usr/bin/env python3

"""
=============================================================
INTRODUCTION TO ALGORITHMS — String Reversal
=============================================================

What is an Algorithm?
    An algorithm is a step-by-step set of instructions for
    solving a problem. Think of it like a recipe — follow
    the steps in order, and you get a predictable result.

The Problem:
    Given a string like "foo bar", return it reversed: "rab oof"

The Plan (Pseudocode):
    1. Start with an original string S  →  "foo bar"
    2. Create an empty list R           →  []
    3. Walk through S backwards,
       adding each character to R       →  ['r', 'a', 'b', ...]
    4. Join R into a single string      →  "rab oof"
    5. Return the result

Why use a list instead of building a string directly?
    Strings in Python are immutable — you can't change them
    in place. Appending to a list and joining at the end is
    much faster for long strings. This is called O(n) time,
    meaning the work grows linearly with the input size.

Try it yourself:
    - Empty string:      ""        →  ""
    - Single character:  "a"       →  "a"
    - Special chars:     "hi!@#"   →  "#@!ih"

Coming up in later chapters:
    This pattern of processing characters one at a time is
    the foundation for palindrome checks, stack problems,
    and more (see Chapter 7).
=============================================================
"""


def reverse_string(original: str) -> str:
    """
    Reverses a string one character at a time.

    Args:
        original: The string you want to reverse.

    Returns:
        A new string with the characters in reverse order.
    """
    reversed_chars = []  # We'll collect characters here as we go backwards

    for char in reversed(original):   # Walk through the string back-to-front
        reversed_chars.append(char)   # Add each character to our list

    return ''.join(reversed_chars)    # Glue the list back into one string


def main():
    sample = "foo bar" # this is the original string we want to reverse
    result = reverse_string(sample)

    print(f'Original : "{sample}"')
    print(f'Reversed : "{result}"')


if __name__ == "__main__":
    main()