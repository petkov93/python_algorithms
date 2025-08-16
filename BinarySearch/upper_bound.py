"""
Use case: Find the first index where the value is strictly greater than target.
Python’s bisect_right does this.
Returns: Insertion position after the last occurrence of target.
"""

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

"""
✅ Problems:
    Rightmost insertion position
    Count occurrences of a number (upper_bound - lower_bound).
"""