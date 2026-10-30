import threading
import time

from main import get_page

posts = [f"post{i}" for i in range(1, 11)]
huge_feed = [f"post{i}" for i in range(1, 2_000_001)]

run_cases = [
    (posts, 1, 3, ["post1", "post2", "post3"], 0.02),
    (posts, 2, 3, ["post4", "post5", "post6"], 0.02),
    (posts, 4, 3, ["post10"], 0.02),
]

submit_cases = run_cases + [
    (posts, 5, 3, [], 0.02),
    (posts, 1, 20, posts, 0.02),
    (posts, 0, 3, [], 0.02),
    (posts, -1, 3, [], 0.02),
    ([], 1, 5, [], 0.02),
    (huge_feed, 19_999, 100, [f"post{i}" for i in range(1_999_801, 1_999_901)], 0.02),
]


def describe(items):
    if len(items) > 10:
        return f"{len(items):,} posts: {items[:2]} ... {items[-1:]}"
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


def do_test(feed, page, page_size, expected_output, time_limit):
    try:
        print("---------------------------------")
        print("Inputs:")
        print(f" * posts: {describe(feed)}")
        print(f" * page: {page}")
        print(f" * page_size: {page_size}")
        print(f"Expected: {describe(expected_output)} in under {time_limit * 1000:.0f} milliseconds")
        finished, result, elapsed = run_with_timeout(get_page, (feed, page, page_size), time_limit)
        if not finished:
            print(f"get_page took longer than {time_limit * 1000:.0f} milliseconds.")
            print("Fail")
            return False
        print(f"Actual:   {describe(result) if isinstance(result, list) else repr(result)}")
        if elapsed > time_limit:
            print(f"get_page took {elapsed * 1000:.1f} milliseconds. Do you need to loop over the whole feed?")
            print("Fail")
            return False
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
