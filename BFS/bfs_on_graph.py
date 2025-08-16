from collections import deque

"""
✅ Used in: “Clone Graph”, “Shortest Path in Unweighted Graph”.
"""

def bfs_graph(graph, start):
    queue = deque([start])
    visited = set([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)   # process node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}
print(bfs_graph(graph, 1))  # [1, 2, 3, 4]
