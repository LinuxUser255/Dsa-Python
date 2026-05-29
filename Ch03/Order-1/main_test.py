from main import *
import time

run_cases = [
    (1000000, "John", "Doe", "Doe999999"),
    (1500000, "Lane", "Wagner", "Wagner1499999"),
]

submit_cases = run_cases + [
    (2000000, "Key", "Error", None),
    (2500000, "Chad", "Energy", "Energy2499999"),
    (3000000, "Tiffany", "Johnson", "Johnson2999999"),
]


def test(complexity, first_name, last_name, expected_output):
    names_dict = get_name_dict(first_name, last_name, complexity)
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * first_name: {first_name}")
    print(f"Expected:  {expected_output} & completed in less than 50 milliseconds")
    if last_name == "Error":
        first_name_key = first_name
    else:
        first_name_key = f"{first_name}{complexity - 1}"
    start = time.time()
    result = find_last_name(names_dict, first_name_key)
    end = time.time()
    timeout = 0.05
    if (end - start) < timeout:
        print(f"find_last_name completed in less than {timeout * 1000} milliseconds!")
        if result == expected_output:
            print(f"Actual: {result}")
            print("Pass")
            return True
        else:
            print(f"Actual: {result}")
            print("Fail")
            return False
    else:
        print(
            f"find_last_name took too long ({(end - start) * 1000} milliseconds). Speed it up!"
        )
        print(f"Actual: {result}")
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


def get_name_dict(first_name, last_name, num):
    names = {}
    for i in range(num):
        names[f"{first_name}{i}"] = f"{last_name}{i}"
    return names


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
