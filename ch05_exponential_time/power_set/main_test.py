from main import power_set

run_cases = [
    ([], [[]]),
    (["python"], [[], ["python"]]),
    (["python", "sql"], [[], ["python"], ["sql"], ["python", "sql"]]),
]

submit_cases = run_cases + [
    (
        ["python", "sql", "go"],
        [
            [],
            ["python"],
            ["sql"],
            ["go"],
            ["python", "sql"],
            ["python", "go"],
            ["sql", "go"],
            ["python", "sql", "go"],
        ],
    ),
    ([1, 2, 3, 4], None),
    (list(range(12)), None),
]


def normalize(subsets):
    """Order doesn't matter, neither between subsets nor inside one, so sort both."""
    return sorted(tuple(sorted(subset)) for subset in subsets)


def do_test(input1, expected_output):
    try:
        print("---------------------------------")
        print("Inputs:")
        print(f" * items: {input1}")
        expected_count = 2 ** len(input1)
        if expected_output is not None:
            print(f"Expected: {expected_output}")
        else:
            print(f"Expected: {expected_count:,} unique subsets (2^{len(input1)})")
        result = power_set(list(input1))
        if result is None:
            print("Actual:   None")
            print("Fail")
            return False
        actual = normalize(result)
        if len(input1) <= 4:
            print(f"Actual:   {result}")
        else:
            print(f"Actual:   {len(result):,} subsets, {len(set(actual)):,} unique")

        if expected_output is not None:
            correct = actual == normalize(expected_output)
        else:
            allowed = set(input1)
            correct = (
                len(actual) == expected_count
                and len(set(actual)) == expected_count
                and all(set(subset) <= allowed for subset in actual)
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
