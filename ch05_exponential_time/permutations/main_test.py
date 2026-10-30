import math

from main import get_orderings

speakers = ["ana", "ben", "cy", "dee", "eve", "fay", "gus"]

run_cases = [
    ([], [[]]),
    (["ana"], [["ana"]]),
    (["ana", "ben"], [["ana", "ben"], ["ben", "ana"]]),
]

submit_cases = run_cases + [
    (
        ["ana", "ben", "cy"],
        [
            ["ana", "ben", "cy"],
            ["ana", "cy", "ben"],
            ["ben", "ana", "cy"],
            ["ben", "cy", "ana"],
            ["cy", "ana", "ben"],
            ["cy", "ben", "ana"],
        ],
    ),
    (speakers[:5], None),
    (speakers, None),
]


def normalize(orderings):
    """The order of the orderings doesn't matter, but the order INSIDE each one does."""
    return sorted(tuple(ordering) for ordering in orderings)


def do_test(input1, expected_output):
    try:
        print("---------------------------------")
        print("Inputs:")
        print(f" * speakers: {input1}")
        expected_count = math.factorial(len(input1))
        if expected_output is not None:
            print(f"Expected: {expected_output}")
        else:
            print(f"Expected: {expected_count:,} unique orderings ({len(input1)}!)")
        result = get_orderings(list(input1))
        if result is None:
            print("Actual:   None")
            print("Fail")
            return False
        actual = normalize(result)
        if len(input1) <= 3:
            print(f"Actual:   {result}")
        else:
            print(f"Actual:   {len(result):,} orderings, {len(set(actual)):,} unique")

        if expected_output is not None:
            correct = actual == normalize(expected_output)
        else:
            correct = (
                len(actual) == expected_count
                and len(set(actual)) == expected_count
                and all(sorted(ordering) == sorted(input1) for ordering in actual)
            )
        if correct:
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
