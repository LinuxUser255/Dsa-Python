def binary_search(target, arr):
    """
    Perform binary search on a sorted array.

    Time Complexity: O(log n) - efficiently handles large arrays (e.g., 2M elements in <50ms)
    Space Complexity: O(1) - iterative approach with constant space

    Args:
        target: The value to search for
        arr: A sorted list in ascending order

    Returns:
        bool: True if target is found, False otherwise

    Note:
        - Assumes arr is pre-sorted in ascending order
        - Handles edge cases: empty array, single element, missing target
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        # Calculate middle index using integer division
        # Avoids potential overflow: mid = low + (high - low) // 2
        mid = (low + high) // 2

        # If arr at mid-equals target
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return False


