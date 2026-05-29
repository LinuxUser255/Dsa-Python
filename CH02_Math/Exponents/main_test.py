from main import *

run_cases = [
    ([7, 4, 3, 100, 765, 2344, 1, 2, 32], 5056),
    ([12, 12, 12], 45),
    ([10, 200, 3000, 5000, 4], 11333),
]

submit_cases = run_cases + [
    ([], 0),
    ([1, 1, 1], 4),
    ([100], 100),
    ([50, 60, 70, 80, 90], 483),
    ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 872),
    (
        [
            5,
            10,
            15,
            20,
            25,
            30,
            35,
            40,
            45,
            50,
            55,
            60,
            65,
            70,
            75,
            80,
            85,
            90,
            95,
            100,
        ],
        1912,
    ),
]


def test(input1, expected_output):
    try:
        print("---------------------------------")
        print(f"Inputs: {input1}")
        result = round(get_estimated_spread(input1))
        print(f"Expected: {expected_output}")
        print(f"Actual:   {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(e)
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
