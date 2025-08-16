def fractional_knapsack(weights, values, capacity):
    """
    Greedy with Sorting Ratios
    E.g., Fractional Knapsack (maximize value with weight limit).
    Take items with the highest value/weight.
    """

    items = sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True)
    total = 0
    for v, w in items:
        if capacity >= w:
            total += v
            capacity -= w
        else:
            total += v * (capacity / w)
            break
    return total

"""
✅ Used in resource allocation.
"""