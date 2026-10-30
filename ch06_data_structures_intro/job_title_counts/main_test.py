from main import count_job_titles

run_cases = [
    (
        [("ana", "Engineer"), ("ben", "Designer"), ("cy", "Engineer")],
        {"Engineer": 2, "Designer": 1},
    ),
    ([], {}),
]

submit_cases = run_cases + [
    ([("ana", "Engineer")], {"Engineer": 1}),
    (
        [
            ("ana", "Engineer"),
            ("ben", "Clerk"),
            ("cy", "Manager"),
            ("dee", "Clerk"),
            ("eve", "Clerk"),
            ("fay", "Manager"),
        ],
        {"Engineer": 1, "Clerk": 3, "Manager": 2},
    ),
    (
        [("ana", "engineer"), ("ben", "Engineer")],
        {"engineer": 1, "Engineer": 1},
    ),
    (
        [(f"user{i}", ["Engineer", "Designer", "Manager", "Clerk", "Analyst"][i % 5]) for i in range(1_003)],
        {"Engineer": 201, "Designer": 201, "Manager": 201, "Clerk": 200, "Analyst": 200},
    ),
]


def describe(users):
    if len(users) > 6:
        return f"{len(users):,} users, starting {users[:2]}..."
    return str(users)


def do_test(input1, expected_output):
    try:
        print("---------------------------------")
        print("Inputs:")
        print(f" * users: {describe(input1)}")
        print(f"Expected: {expected_output}")
        result = count_job_titles(input1)
        print(f"Actual:   {result}")
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
