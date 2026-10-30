from main import get_num_guesses

run_cases = [
    (1, 26),
    (2, 702),
    (3, 18_278),
]

submit_cases = run_cases + [
    (0, 0),
    (4, 475_254),
    (5, 12_356_630),
    (8, 217_180_147_158),
    (10, 146_813_779_479_510),
]


def do_test(input1, expected_output):
    try:
        print("---------------------------------")
        print("Inputs:")
        print(f" * max password length: {input1}")
        print(f"Expected: {expected_output:,}")
        result = get_num_guesses(input1)
        print(f"Actual:   {result:,}" if isinstance(result, int) else f"Actual:   {result!r}")
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
