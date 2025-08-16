"""
Binary search on answer, a.k.a. Search Space

Use case: When you can’t directly search an array, but you can check a condition (is_possible(x)).
Idea: Search the space of possible answers instead of array indices.
"""

def binary_search_answer(low, high, condition):
    while low < high:
        mid = (low + high) // 2
        if condition(mid):
            high = mid  # condition holds, try smaller
        else:
            low = mid + 1
    return low


"""
✅Problems:
"Koko Eating Bananas" 🍌
"Minimum Capacity to Ship Packages in D Days"
"Aggressive Cows" (classic)"""