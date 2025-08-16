"""
Used in: "Clone Graph", "Number of Connected Components".
"""

def dfs_graph(graph, start):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)   # process node
        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(start)
    return result

graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}
print(dfs_graph(graph, 1))  # [1,2,4,3]
