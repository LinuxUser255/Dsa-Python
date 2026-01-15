#!/usr/bin/env python3

"""
Try this:
Here's some pseudocode for a mystery algorithm:

Start with an original string called S
and a new empty string called R.

Loop through S from its last character
to its first character,

and for each char, add it to the end of R.
sequence.append(value, /)¶
Append value to the end of the sequence
This is equivalent to writing
seq[len(seq):len(seq)] = [value].

Once you’ve processed all the characters,
return R.

Quick Tips for Improvement:

Efficiency: For long strings, this list-append-join approach is optimal (O(n) time),
            avoiding slow string concatenation.

Edge Cases: Test with empty ("" → ""), single char ("a" → "a"), or
            special chars ("hello!@#").

Alternatives: Python's slicing (return input_str[::-1]) is idiomatic,
                but your loop builds algorithmic thinking—key for DSA
                like palindromes or stacks (Chapter 7).

Modularity: In your projects, wrap this in a class method for reuse.

"""


def loop_char():
    # need to loop backwards to reverse the string
    s = "foo bar"
    R = []  # initialize `r` as an empty list to store reversed string

    input_str = s

    input_str = list(input_str)

    for char in reversed(input_str):
        R.append(char)  # append each character to the end of the reversed string

    return ''.join(R)


def main():
    """call the loop_char() function within the print function"""
    print(f'foo bar reversed:  {loop_char()}  \n')
    #print(loop_char())


if __name__ == "__main__":
    main()
