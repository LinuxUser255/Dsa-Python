#!/usr/bin/env python3
"""
How memoization turns an exponential recursion into a polynomial one.

Problem: on a grid with `rows` x `cols` cells, you start in the top-left corner
and may only move RIGHT or DOWN. How many different paths reach the bottom-right?

Recursive idea: the paths to a cell = paths to the cell above + paths to the cell on the left.
That's two recursive calls that overlap heavily, so the naive version repeats work exponentially.
"""

calls = 0


def grid_paths_naive(rows, cols):
    global calls
    calls += 1
    if rows == 1 or cols == 1:
        return 1
    return grid_paths_naive(rows - 1, cols) + grid_paths_naive(rows, cols - 1)


def grid_paths_memo(rows, cols, memo=None):
    global calls
    calls += 1
    if memo is None:
        memo = {}
    if (rows, cols) in memo:
        return memo[(rows, cols)]
    if rows == 1 or cols == 1:
        return 1
    answer = grid_paths_memo(rows - 1, cols, memo) + grid_paths_memo(rows, cols - 1, memo)
    memo[(rows, cols)] = answer
    return answer


def main():
    global calls
    print(f"{'grid':>7} | {'paths':>12} | {'naive calls':>12} | {'memo calls':>10}")
    print("-" * 52)
    for size in (8, 9, 10, 11, 12):
        calls = 0
        paths = grid_paths_naive(size, size)
        naive_calls = calls

        calls = 0
        grid_paths_memo(size, size)
        memo_calls = calls

        print(f"{size:>3}x{size:<3} | {paths:>12,} | {naive_calls:>12,} | {memo_calls:>10,}")

    print("\nNaive calls grow about 4x per +1 grid size: exponential.")
    print("Memoized calls grow like size^2: there are only rows*cols different questions to answer,")
    print("and each one is answered exactly once.")


if __name__ == "__main__":
    main()
