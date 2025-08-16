def min_meeting_rooms(intervals):
    """
    Meeting Rooms (Min Rooms Required)
    Greedy with two sorted lists.
    """
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)

    s = e = rooms = 0
    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1
            s += 1
        else:
            e += 1
            s += 1
    return rooms

"""
✅ Used in booking systems, concurrency.
"""