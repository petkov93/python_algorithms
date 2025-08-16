"""
✅ Used in: "Number of Islands", "Flood Fill", "Max Area of Island".
"""


def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == "0" or
                (r, c) in visited):
            return
        visited.add((r, c))
        # explore 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                islands += 1
    return islands
