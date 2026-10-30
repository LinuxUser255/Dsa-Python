import random
import threading
import time

from main import build_user_index, get_users_by_ids

JOB_TITLES = ["Engineer", "Designer", "Manager", "Clerk", "Analyst"]


def get_users(num):
    """User ids go up in steps of 3 (0, 3, 6, ...), so an id is NOT a list position."""
    users = []
    for i in range(num):
        user_id = i * 3
        users.append((user_id, f"user{i}", JOB_TITLES[i % len(JOB_TITLES)]))
    random.seed(12)
    random.shuffle(users)
    return users


def expected_user(user_id, num):
    if user_id % 3 != 0 or not 0 <= user_id < num * 3:
        return None
    i = user_id // 3
    return (user_id, f"user{i}", JOB_TITLES[i % len(JOB_TITLES)])


small_users = [
    (7, "ana", "Engineer"),
    (3, "ben", "Designer"),
    (42, "cy", "Manager"),
]

num_large = 300_000
large_users = get_users(num_large)
random.seed(13)
large_ids = [random.randrange(0, num_large * 3 + 1_000) for _ in range(10_000)]

run_cases = [
    (small_users, [7, 42], [(7, "ana", "Engineer"), (42, "cy", "Manager")], 2.0, 0.1),
    (small_users, [99], [None], 2.0, 0.1),
]

submit_cases = run_cases + [
    (small_users, [], [], 2.0, 0.1),
    ([], [1, 2], [None, None], 2.0, 0.1),
    (small_users, [3, 3, 8, 7], [(3, "ben", "Designer"), (3, "ben", "Designer"), None, (7, "ana", "Engineer")], 2.0, 0.1),
    (large_users, large_ids, [expected_user(user_id, num_large) for user_id in large_ids], 2.0, 0.1),
]


def describe(items):
    if len(items) > 6:
        return f"{len(items):,} items, starting {items[:2]}..."
    return str(items)


def run_with_timeout(func, args, timeout):
    """
    Runs func(*args) on a background thread so a too-slow solution
    can't hang the whole test run.
    Returns (finished, result, seconds).
    """
    outcome = {}

    def target():
        try:
            outcome["result"] = func(*args)
        except Exception as e:
            outcome["error"] = e

    start = time.perf_counter()
    worker = threading.Thread(target=target, daemon=True)
    worker.start()
    worker.join(timeout)
    elapsed = time.perf_counter() - start
    if worker.is_alive():
        return False, None, elapsed
    if "error" in outcome:
        raise outcome["error"]
    return True, outcome.get("result"), elapsed


def do_test(users, ids, expected_output, build_limit, lookup_limit):
    try:
        print("---------------------------------")
        print("Inputs:")
        print(f" * users: {describe(users)}")
        print(f" * ids to look up: {describe(ids)}")
        print(f"Expected: {describe(expected_output)}")

        finished, index, build_time = run_with_timeout(build_user_index, (list(users),), build_limit)
        if not finished:
            print(f"build_user_index took longer than {build_limit}s.")
            print("Fail")
            return False
        print(f"build_user_index: {build_time:.4f}s")

        finished, result, lookup_time = run_with_timeout(get_users_by_ids, (index, list(ids)), lookup_limit)
        if not finished:
            print(f"get_users_by_ids took longer than {lookup_limit * 1000:.0f} milliseconds for {len(ids):,} lookups.")
            print("Is each lookup O(1)?")
            print("Fail")
            return False
        print(f"get_users_by_ids: {lookup_time * 1000:.2f} milliseconds")
        print(f"Actual:   {describe(result) if isinstance(result, list) else repr(result)}")
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
