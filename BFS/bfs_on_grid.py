"""
Most common LeetCode usage.
We expand in 4 (or 8) directions using a queue.
"""

def shortest_path(grid, start, end):
    from collections import deque
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start[0], start[1], 0)])  # (r, c, distance)
    visited.add(start)

    while queue:
        r, c, dist = queue.popleft()
        if (r, c) == end:
            return dist
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                grid[nr][nc] == 0 and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc, dist+1))
    return -1


"""
✅ Used in: “Shortest Path in Binary Matrix”, “Rotting Oranges”, “Walls and Gates”.
"""