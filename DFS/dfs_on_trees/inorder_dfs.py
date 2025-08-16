"""
Inorder DFS (Left → Root → Right)
Process left, then current, then right.
Special for BSTs: gives sorted order.

✅ Used in: “Validate BST”, “Kth Smallest Element in BST”.
"""

def inorder(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)   # process in the middle
        dfs(node.right)
    dfs(root)
    return result
