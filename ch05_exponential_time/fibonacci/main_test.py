import threading
import time

from main import fib

run_cases = [
    (0, 0, 0.05),
    (1, 1, 0.05),
    (2, 1, 0.05),
    (10, 55, 0.05),
]

submit_cases = run_cases + [
    (20, 6_765, 0.05),
    (25, 75_025, 0.05),
    (32, 2_178_309, 0.05),
    (50, 12_586_269_025, 0.05),
    (90, 2_880_067_194_370_816_120, 0.05),
]


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
        print(f" * n: {input1}")
        print(f"Expected: {expected_output:,} in under {time_limit * 1000:.0f} milliseconds")
        finished, result, elapsed = run_with_timeout(fib, (input1,), time_limit)
        if not finished:
            print(f"fib({input1}) took longer than {time_limit * 1000:.0f} milliseconds. Speed it up!")
            print("Fail")
            return False
        print(f"Actual:   {result:,}" if isinstance(result, int) else f"Actual:   {result!r}")
        print(f"Time:     {elapsed * 1000:.2f} milliseconds")
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
