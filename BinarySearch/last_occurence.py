from BinarySearch.lower_bound import lower_bound
from BinarySearch.upper_bound import upper_bound

# Sometimes arrays have duplicates, and you need the first or last index of a target.

def leftmost(arr, target):
    idx = lower_bound(arr, target)
    return idx if idx < len(arr) and arr[idx] == target else -1

def rightmost(arr, target):
    idx = upper_bound(arr, target) - 1
    return idx if idx >= 0 and arr[idx] == target else -1


"✅ Problems: Find First and Last Position of Element in Sorted Array."