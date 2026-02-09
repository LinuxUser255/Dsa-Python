from main import *

run_cases = [
    ([["George", "Eva", "George"], ["Diane", "George", "Eva", "Frank"]], "George", 3),
    (
        [
            ["Amy", "Bob", "Candy"],
            ["Diane", "George", "Eva", "Frank"],
            ["Diane", "George"],
            ["George", "name", "George"],
        ],
        "George",
        4,
    ),
]

submit_cases = run_cases + [
    (
        [
            ["Alex", "name", "Chloe"],
            ["Eric", "name", "Fred"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["George"],
        ],
        "Hector",
        3,
    ),
    (
        [
            ["Alex", "name", "Chloe"],
            ["Eric", "name", "Fred"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["Hector", "name"],
            ["George"],
        ],
        "George",
        1,
    ),
    (
        [["Alex", "name", "Chloe"], ["Eric", "name", "Fred"], ["Hector", "name"]],
        "Alex",
        1,
    ),
    ([], "George", 0),
]


def do_test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * list of lists: {input1}")
    print(f" * target name: {input2}")
    result = count_names(input1, input2)
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
    skipped = len(submit_cases) - len(do_test_cases)
    for do_test_case in do_test_cases:
        correct = do_test(*do_test_case)
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


do_test_cases = submit_cases
if "__RUN__" in globals():
    do_test_cases = run_cases

main()
