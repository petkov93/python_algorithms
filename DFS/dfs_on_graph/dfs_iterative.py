"""
DFS Iterative (Using Stack)
Sometimes recursion depth is an issue, so we use a stack manually.

✅ Used when recursion may hit limits (Python recursion ~1000 depth).
"""

def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    result = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        # push neighbors
        for neighbor in reversed(graph[node]):
            stack.append(neighbor)

    return result
