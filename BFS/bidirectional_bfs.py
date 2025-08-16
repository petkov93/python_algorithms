def bidirectional_bfs(graph, start, end):
    from collections import deque
    """
    Used for shortest path in huge graphs. Start BFS from both ends and meet in the middle.
    """
    if start == end: return 0
    q1, q2 = {start}, {end}
    visited1, visited2 = {start}, {end}
    steps = 0

    while q1 and q2:
        steps += 1
        if len(q1) > len(q2):  # expand smaller frontier
            q1, q2 = q2, q1
            visited1, visited2 = visited2, visited1
        new_q = set()
        for node in q1:
            for nei in graph[node]:
                if nei in visited2:
                    return steps
                if nei not in visited1:
                    visited1.add(nei)
                    new_q.add(nei)
        q1 = new_q
    return -1

"""
✅ Used in: “Word Ladder” (classic).
"""