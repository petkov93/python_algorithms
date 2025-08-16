def max_sum_subarray(nums, k):
    """
    Window size stays constant.
    Common in averages, sums.
    """
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k]  # slide right
        max_sum = max(max_sum, window_sum)
    return max_sum

"""
✅ Used in: “Maximum Sum Subarray of Size K”, “Moving Average”.
"""
