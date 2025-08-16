"""
DFS Path Accumulation (Root → Leaf)

✅ Used in: “Binary Tree Paths”, “Path Sum II”.
"""

def all_paths(root):
    result = []
    def dfs(node, path):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:  # leaf
            result.append(path[:])  # copy
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()  # backtrack
    dfs(root, [])
    return result
