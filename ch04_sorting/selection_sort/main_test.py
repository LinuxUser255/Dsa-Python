import random

from main import selection_sort


def get_random_nums(num):
    random.seed(11)
    return [random.randint(0, 10_000) for _ in range(num)]


medium_nums = get_random_nums(1_000)

run_cases = [
    ([5, 7, 3, 6, 8], [3, 5, 6, 7, 8]),
    ([2, 1], [1, 2]),
    ([], []),
]

submit_cases = run_cases + [
    ([1], [1]),
    ([1, 5, -3, 2, 4], [-3, 1, 2, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 2, 3, 5, 4], [1, 2, 3, 4, 5]),
    ([3, 1, 3, 2, 1], [1, 1, 2, 3, 3]),
    (medium_nums, sorted(medium_nums)),
]


def describe(nums):
    if len(nums) > 20:
        return f"{len(nums)} numbers, starting {nums[:5]}..."
    return str(nums)


def do_test(input1, expected_output):
    try:
        print("---------------------------------")
        print(f"Input:\n * {describe(input1)}")
        print(f"Expected: {describe(expected_output)}")
        nums = list(input1)
        result = selection_sort(nums)
        print(f"Actual:   {describe(result) if result is not None else None}")
        if result is not nums:
            print("selection_sort must sort the list *in place* and return that same list")
            print("Fail")
            return False
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
