def min_window(s, t):
    """
    Minimum Window Substring
    Classic hard one → shrink window while it still satisfies condition.
    """
    from collections import Counter
    need = Counter(t)
    missing = len(t)
    left = start = end = 0

    for right, ch in enumerate(s, 1):  # right is 1-based
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1

        if missing == 0:  # valid window
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if end == 0 or right - left < end - start:
                start, end = left, right
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]

"""
✅ Used in: “Minimum Window Substring”, “Smallest Subarray with Sum ≥ K”.
"""