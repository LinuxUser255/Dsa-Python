import random
import threading
import time

from main import merge_sort


def get_random_nums(num):
    random.seed(4)
    return [random.randint(-1_000_000, 1_000_000) for _ in range(num)]


large_nums = get_random_nums(20_000)

run_cases = [
    ([5, 7, 3, 6, 8], [3, 5, 6, 7, 8], 1.0),
    ([2, 1], [1, 2], 1.0),
    ([], [], 1.0),
]

submit_cases = run_cases + [
    ([1], [1], 1.0),
    ([1, 5, -3, 2, 4], [-3, 1, 2, 4, 5], 1.0),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], 1.0),
    ([4, 1, 4, 2, 1, 4], [1, 1, 2, 4, 4, 4], 1.0),
    (large_nums, sorted(large_nums), 1.0),
]


def describe(nums):
    if len(nums) > 20:
        return f"{len(nums)} numbers, starting {nums[:5]}..."
    return str(nums)


def run_with_timeout(func, args, timeout):
    """
    Runs func(*args) on a background thread so a too-slow solution
    can't hang the whole test run.
    Returns (finished, result, seconds).
    """
    outcome = {}

    def target():
        try:
            outcome["result"] = func(*args)
        except Exception as e:
            outcome["error"] = e

    start = time.perf_counter()
    worker = threading.Thread(target=target, daemon=True)
    worker.start()
    worker.join(timeout)
    elapsed = time.perf_counter() - start
    if worker.is_alive():
        return False, None, elapsed
    if "error" in outcome:
        raise outcome["error"]
    return True, outcome.get("result"), elapsed


def do_test(input1, expected_output, time_limit):
    try:
        print("---------------------------------")
        print(f"Input:\n * {describe(input1)}")
        print(f"Expected: {describe(expected_output)} in under {time_limit}s")
        finished, result, elapsed = run_with_timeout(
            merge_sort, (list(input1),), time_limit
        )
        if not finished:
            print(f"merge_sort took longer than {time_limit}s. Is it really O(n log n)?")
            print("Fail")
            return False
        print(f"Actual:   {describe(result) if result is not None else None}")
        print(f"Time:     {elapsed:.4f}s")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(f"Error: {e!r}")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = do_test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

if __name__ == "__main__":
    main()
