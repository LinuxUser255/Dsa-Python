import random
import threading
import time

from main import get_mutual_connections


def get_large_networks():
    """Two networks of 100,000 users each that overlap on user50000 through user99999."""
    random.seed(8)
    first = [f"user{i}" for i in range(0, 100_000)]
    second = [f"user{i}" for i in range(50_000, 150_000)]
    random.shuffle(first)
    random.shuffle(second)
    return first, second


large_a, large_b = get_large_networks()

run_cases = [
    (["ana", "ben", "cy"], ["cy", "dee", "ana"], ["ana", "cy"], 1.0),
    (["ana"], ["ben"], [], 1.0),
]

submit_cases = run_cases + [
    ([], ["ana"], [], 1.0),
    (["ana", "ben"], [], [], 1.0),
    (["ana", "ana", "ben"], ["ana", "ana"], ["ana"], 1.0),
    (["eve", "dee", "cy", "ben"], ["ben", "cy", "dee", "eve"], ["ben", "cy", "dee", "eve"], 1.0),
    (large_a, large_b, sorted(f"user{i}" for i in range(50_000, 100_000)), 1.0),
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


def do_test(input1, input2, expected_output, time_limit):
    try:
        print("---------------------------------")
        print("Inputs:")
        print(f" * connections_a: {describe(input1)}")
        print(f" * connections_b: {describe(input2)}")
        print(f"Expected: {describe(expected_output)} in under {time_limit}s")
        finished, result, elapsed = run_with_timeout(
            get_mutual_connections, (list(input1), list(input2)), time_limit
        )
        if not finished:
            print(f"get_mutual_connections took longer than {time_limit}s. Is it O(n + m)?")
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
