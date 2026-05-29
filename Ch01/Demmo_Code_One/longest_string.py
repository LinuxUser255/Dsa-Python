#!/usr/bin/env python3

list_of_words = [
    "Elephant",
    "Banana",
    "Computer",
    "Lime",
    "Microphone",
    "Galaxy",
]


def find_longest_string(lst):
    longest_so_far = ""

    for s in lst:
        if len(s) > len(longest_so_far):
            longest_so_far = s

    return longest_so_far


def main():
    print(find_longest_string(list_of_words))


if __name__ == "__main__":
    main()
