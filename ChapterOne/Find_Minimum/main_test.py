
from main import *

run_cases = [
    ([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 1),
    ([12, 12, 12], 12),
    ([10, 200, 3000, 5000, 4], 4),
]

submit_cases = run_cases + [
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([5, 4, 3, 2, 1], 1),
    ([100, 200, 300, 400, 500], 100),
    ([500, 400, 300, 200, 100], 100),
    ([], None),
]


def test(input1, expected_output):
    """Tests the `find_minimum(nums): function from main.py
       with a given input and expected output.

    Args:
        input1 (list): A list of numbers to be passed to the find_minimum function.
        expected_output (any): The expected minimum value from the input list.

    Returns:
        bool: True if the actual result from find_minimum matches the
              expected_output, False otherwise.
    """
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = find_minimum(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    """Runs the test suite and prints a summary of the results.

    This function iterates through a list of test cases, either `run_cases` or
    the full `submit_cases` list, and executes them using the `test` function.
    It counts the number of passed and failed tests and prints a summary
    to the console, including the number of skipped tests if applicable.
    """
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
    # test_cases is the variable that contains the result of run_cases()
    # run_cases is the first list of numbers
    # it's passed to the find_minimum function
    # test_cases is the second list of numbers
    # to be passed to the find_minimum function

main()
