import random
import threading
import time

from main import find_duplicate_handles


def get_signup_log():
    """200,000 sign-ups where user0 through user49999 each signed up twice."""
    random.seed(6)
    handles = [f"user{i % 150_000}" for i in range(200_000)]
    random.shuffle(handles)
    return handles


signup_log = get_signup_log()

run_cases = [
    (["ana", "ben", "ana"], ["ana"], 1.0),
    (["ana", "ben", "cy"], [], 1.0),
    ([], [], 1.0),
]

submit_cases = run_cases + [
    (["x", "y", "x", "x", "y", "z"], ["x", "y"], 1.0),
    (["Ana", "ana"], [], 1.0),
    (["dee", "cy", "dee", "ben", "cy", "ana"], ["cy", "dee"], 1.0),
    (signup_log, sorted(f"user{i}" for i in range(50_000)), 1.0),
]


def describe(handles):
    if len(handles) > 10:
        return f"{len(handles):,} handles, starting {handles[:3]}..."
    return str(handles)


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


def do_test(input1, expected_output, time_limit):
    try:
        print("---------------------------------")
        print("Inputs:")
        print(f" * handles: {describe(input1)}")
        print(f"Expected: {describe(expected_output)} in under {time_limit}s")
        finished, result, elapsed = run_with_timeout(
            find_duplicate_handles, (list(input1),), time_limit
        )
        if not finished:
            print(f"find_duplicate_handles took longer than {time_limit}s. Is it O(n)?")
            print("Fail")
            return False
        print(f"Actual:   {describe(result) if isinstance(result, list) else repr(result)}")
        print(f"Time:     {elapsed:.4f}s")
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
