
O(n^2)
```python
def bubble_sort(nums: list[int]) -> list[int]:
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                temp = nums[i - 1]
                nums[i - 1] = nums[i]
                nums[i] = temp
                swapping = True
        end -= 1
    return nums
```

**Best case: O(n)**

This is when the list is *already sorted*. Your implementation handles this efficiently because of the `swapping` flag. On the first pass through the `for` loop, no swaps happen, so `swapping` stays `False`, and the `while` loop exits immediately after just one full scan.

One pass through n elements = O(n).

**Worst case: O(n²)**

This is when the list is in *reverse order* — like `[9, 8, 7, 6, 5]`. Every single comparison requires a swap, and the largest unsorted element has to bubble all the way to the end on every pass.

You end up doing roughly:
```
pass 1: n-1 comparisons
pass 2: n-2 comparisons
pass 3: n-3 comparisons
...
```
Which adds up to about n²/2 operations — simplified to O(n²).

---

This is why bubble sort is mostly a *teaching tool* and not used in production. Python's built-in `sorted()` is O(n log n) in the worst case, which is dramatically faster on large datasets. For example at n=1000:

- O(n²) → ~1,000,000 operations
- O(n log n) → ~10,000 operations

The `swapping` flag optimization you implemented is what gives bubble sort its O(n) best case — without it, it would be O(n²) even on an already sorted list.