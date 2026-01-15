from main import *

run_cases = [([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2343243), ([12, 12, 12], 12)]

submit_cases = run_cases + [
    ([10, 200, 3000, 5000, 4], 5000),
    ([0], 0),
    ([-1, -2, -3], -1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * nums: {input1}")
    result = find_max(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
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

main()
