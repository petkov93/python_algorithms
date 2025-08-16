def two_sum_sorted(arr, target):
    """
    Start one pointer at the beginning, one at the end.
    Move inward based on conditions.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            return (left, right)
        elif curr < target:
            left += 1
        else:
            right -= 1
    return None

"""
✅ Used in: “Two Sum II”, “Container With Most Water”.
"""