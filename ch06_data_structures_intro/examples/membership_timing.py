#!/usr/bin/env python3
"""
`x in list` is O(n). `x in set` and `x in dict` are O(1) on average.

Times 1,000 membership checks against containers of growing size.
The worst case for a list is a value that isn't there, so half of the
lookups below are misses.
"""

import random
import timeit


def main():
    random.seed(3)
    print(f"{'n':>10} | {'list':>10} | {'set':>10} | {'dict':>10} | list / set")
    print("-" * 62)
    for n in (1_000, 10_000, 100_000, 1_000_000):
        handles = [f"user{i}" for i in range(n)]
        as_set = set(handles)
        as_dict = dict.fromkeys(handles)
        lookups = [f"user{random.randrange(n * 2)}" for _ in range(1_000)]

        list_time = timeit.timeit(lambda: [h in handles for h in lookups], number=1)
        set_time = timeit.timeit(lambda: [h in as_set for h in lookups], number=1)
        dict_time = timeit.timeit(lambda: [h in as_dict for h in lookups], number=1)
        print(
            f"{n:>10,} | {list_time:>9.4f}s | {set_time:>9.5f}s | {dict_time:>9.5f}s | {list_time / set_time:>8,.0f}x"
        )

    print("\nThe list column grows about 10x per row (O(n) per lookup).")
    print("The set and dict columns barely move (O(1) per lookup).")
    print("Building the set costs O(n) once. Worth it if you look things up more than a handful of times.")


if __name__ == "__main__":
    main()
