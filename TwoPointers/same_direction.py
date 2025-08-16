def is_subsequence(s, t):
    """
    Both pointers move forward, but at different speeds.
    Used to compare subsequences.
    Example: Check if s is subsequence of t
    """
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

"""
✅ Used in: “Is Subsequence”, “Merge Two Sorted Lists”.
"""