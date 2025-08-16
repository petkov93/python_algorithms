"""
Use case: Find the first index where the value is greater than or equal to the target.
Python’s bisect_left does exactly this.
Returns: Index where target should be inserted to keep array sorted.
# from bisect import bisect_left
# lst = [20, 30, 40, 50, 60]
# print(bisect_left(lst, 35))
"""
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

"""
✅Possible Problems:
    First Bad Version
    Ceiling of a number
    Search Insert Position
"""