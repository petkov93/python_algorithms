"""
Idea:
    Compute the cumulative sum (or other operation) of an array
    so that you can quickly query sums of subarrays.
Example:
    Given an array [2, 1, 5, 3],
    build a prefix sum array where prefix[i] = sum of elements
    from arr[0] to arr[i-1].
Steps:
    Initialize prefix[0] = 0
    For each index i: prefix[i+1] = prefix[i] + arr[i]
    Subarray sum from l to r → prefix[r+1] - prefix[l]
"""
nums = [2, 1, 5, 3]
prefix = [0] * (len(nums) + 1)

for i in range(len(nums)):
    prefix[i+1] = prefix[i] + nums[i]

# Query: sum of elements from index 1 to 3
subarray_sum = prefix[4] - prefix[1]  # 1 + 5 + 3 = 9
print(subarray_sum)

"""
Use Cases:
    Fast subarray sum queries
    Count number of subarrays with a given sum
    Range update / range query problems
    2D prefix sums for matrices (image processing, sum of rectangle)
"""