"""
Recursion Uses the Call Stack (LIFO)

When a function calls itself recursively,
each call is pushed onto the call stack like adding a plate to the top of the pile:

countdown(5)     ← top of stack (most recent call)
countdown(4)
countdown(3)
countdown(2)
countdown(1)
countdown(0)     ← bottom (first to finish)

"""


def countdown(n):
    """
    Recursively counts down from n to 0, printing each number.

    - Base case: stops when n <= 0
    - Recursive case: prints n and calls itself with n-1
    """
    if n <= 0:  # Base case: stops recursion to prevent infinite loop
        print("Done!")
    else:  # Recursive case: continue with smaller problem
        print(n)  # Print current value (5, 4, 3, 2, 1)
        countdown(n - 1)  # Recursive call: pushes new frame onto call stack


# Name Guarding: Only runs this script when this file is executed directly (not when imported)
if __name__ == "__main__":
    # Initial call that starts the recursion
    # Argument `5` binds to parameter `n` in the first call
    countdown(5)


#def countdown(n):
#    """
#    Recursively counts down from n to 0.
#
#    Base case stops the recursion; recursive case reduces the problem size.
#    """
#    if n <= 0:  # Base case: stops recursion to prevent infinite loop
#        print("Done!")
#    else:  # Recursive case: keep going with a smaller problem
#        print(n)  # Print the current value (5, 4, 3, 2, 1)
#        countdown(n - 1)  # Recursive call: pushes a new frame onto the call stack
#
#
## Initial call that starts everything
#
#if __name__ == "__main__":
#    countdown(5)  # Argument 5 is bound to parameter n in the first call


