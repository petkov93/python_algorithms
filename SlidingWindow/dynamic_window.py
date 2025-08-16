def longest_substring_k_distinct(s, k):
    """
    Dynamic-Size Window (Expand + Shrink)
    Window grows with right, shrinks with left when condition breaks.
    Common in substring problems.
    """
    from collections import Counter
    count = Counter()
    left, max_len = 0, 0

    for right, ch in enumerate(s):
        count[ch] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len

"""
✅ Used in:
“Longest Substring Without Repeating Characters”
“Longest Substring with K Distinct Characters”
"""