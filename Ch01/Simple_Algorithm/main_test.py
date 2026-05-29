from main import *
# ChapterOne/Simple_Algorithm/main_test.pyv
# Define the test cases as a list of tuples,
# where each tuple contains a list of numbers and the expected sum
# Each tuple has two parts:
#
# First part → the input list (this becomes input1)
# Second part → the correct expected sum (this becomes expected_output)
run_cases = [
    (    # input1 = {list: 9} [the list of numbers below]
        [7, 4, 3, 100, 2343243, 343434, 1, 2, 32],
        2686826
    ),
    (
        [12, 12, 12],
        # these numbers are what get  passed to my summed function
        36 # input1 = [12, 12, 12] => total = 36
    ),
]

# for full evaluation
submit_cases = run_cases + [
    ([10, 200, 3000, 5000, 4], 8214),
    ([], 0),
    ([1], 1),
    ([123456789], 123456789),
    ([-1, -2, -3], -6),
    ([0, 0, 0, 0, 0], 0),
]


def test(input1, expected_output):
    # input1: The list of numbers to pass to
    # your summed function.
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * nums: {input1}")
    # my function call from main.py
    # the result is the sum of the input list
    result = summed(input1)
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
    # Second part → correct expected sum → becomes
    # expected_output calced' here
    for test_case in test_cases:
        # calling the test() function , with 2 args
        # input1 and expected_output
        # def test(input1, expected_output):
        # the * unpacks each tuple
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
    """
    run it locally in “Run” mode, you see 2 tests + “skipped” 
    note. 
    When you submit, all 8 run silently in the background 
    for grading.
    """
    test_cases = run_cases

main()
