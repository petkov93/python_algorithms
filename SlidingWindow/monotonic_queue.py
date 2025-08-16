from collections import deque

def sliding_window_max(nums, k):
    """
    Sliding Window with Monotonic Queue
    Optimized variant for problems like “sliding window maximum”.
    Keeps max/min in O(1) time per step.
    """
    dq = deque()
    result = []
    for i, n in enumerate(nums):
        # remove smaller elements
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)

        # remove out-of-window indices
        if dq[0] == i - k:
            dq.popleft()

        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

"""
✅ Used in: “Sliding Window Maximum”.
"""