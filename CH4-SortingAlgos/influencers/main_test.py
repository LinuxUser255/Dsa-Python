
# Step 1: Import everything from your main.py
from main import *

# Step 2: Create Influencer objects with the appropriate number of selfies and bio links
theprimeagen = Influencer(100, 1)
pokimane = Influencer(800, 2)
spambot = Influencer(0, 200)
lane = Influencer(10, 2)
badcop = Influencer(1, 2)

# Step 3: Test Cases Setup, Creating test objects using the Influencer class from main.py
run_cases = [
    ([badcop, lane], [badcop, lane]),
    ([lane, badcop, pokimane], [badcop, lane, pokimane]),
    ([spambot, theprimeagen], [theprimeagen, spambot]),
]

submit_cases = run_cases + [
    ([], []),
    ([lane], [lane]),
    (
        [pokimane, theprimeagen, spambot, badcop, lane],
        [badcop, lane, theprimeagen, pokimane, spambot],
    ),
]

# Step 4: Test execution
def do_test(input1, expected_output):
    print("---------------------------------")
    print(f"Input:\n * {input1}")
    print(f"Expected: {expected_output}")
    result = vanity_sort(input1) # <-- Calls My function from main.py
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(do_test_cases)
    for do_test_case in do_test_cases:
        correct = do_test(*do_test_case)
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


do_test_cases = submit_cases
if "__RUN__" in globals():
    do_test_cases = run_cases

main()
