def move_zeroes(nums):
    """Partitioning / Dutch National Flag
    Swap elements while moving two pointers around a pivot.
    Example: Move zeroes to end
    """
    non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero], nums[i] = nums[i], nums[non_zero]
            non_zero += 1
    return nums


print(move_zeroes([0, 0, 0, 1, 1, 1]))

"""
✅ Used in: “Sort Colors”, “Move Zeroes”
"""
