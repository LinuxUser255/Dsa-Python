import random
import threading
import time

from main import quick_sort


def get_random_nums(num):
    random.seed(5)
    return [random.randint(-1_000_000, 1_000_000) for _ in range(num)]


large_nums = get_random_nums(20_000)

run_cases = [
    ([9, 3, 7, 1, 5], [1, 3, 5, 7, 9], 1.0),
    ([2, 1], [1, 2], 1.0),
    ([], [], 1.0),
]

submit_cases = run_cases + [
    ([1], [1], 1.0),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 1.0),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5], 1.0),
    ([4, 1, 4, 2, 1, 4], [1, 1, 2, 4, 4, 4], 1.0),
    ([0, -5, 12, -5, 7, 3, 0], [-5, -5, 0, 0, 3, 7, 12], 1.0),
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
        nums = list(input1)
        finished, _, elapsed = run_with_timeout(
            quick_sort, (nums, 0, len(nums) - 1), time_limit
        )
        if not finished:
            print(f"quick_sort took longer than {time_limit}s.")
            print("Fail")
            return False
        # quick_sort returns nothing: it rearranges `nums` itself
        print(f"Actual:   {describe(nums)}")
        print(f"Time:     {elapsed:.4f}s")
        if nums == expected_output:
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
