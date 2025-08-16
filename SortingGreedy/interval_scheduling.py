def max_non_overlapping(intervals):
    """
    Interval Scheduling (Max Non-Overlapping Intervals)
    Pick max number of activities you can attend without overlap.
    Greedy: always take the earliest finishing activity.
    """
    intervals.sort(key=lambda x: x[1])  # sort by end
    count, end = 0, float('-inf')

    for start, finish in intervals:
        if start >= end:
            count += 1
            end = finish
    return count

"""
✅ Classic in scheduling, CPU task allocation.
"""