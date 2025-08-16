"""
Binary Search in Rotated Array
Use case: Sorted array rotated at some pivot.
Idea: Still O(log n), but check which side is sorted each step.
"""

def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:  # left sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

"✅ Problems: Search in Rotated Sorted Array."