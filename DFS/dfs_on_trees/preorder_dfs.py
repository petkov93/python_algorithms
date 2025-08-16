"""
Preorder DFS (Root → Left → Right)
Process the current node first, then go down.

✅ Used in: “Serialize / Deserialize Tree”, “Clone Tree”.
"""

def preorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)    # process root first
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return result