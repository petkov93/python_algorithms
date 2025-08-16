"""
3. Postorder DFS (Left → Right → Root)
Process children first, then the parent.

✅ Used in: “Evaluate Expression Tree”, “Delete Node in Tree”.
"""

def postorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)   # process last
    dfs(root)
    return result
