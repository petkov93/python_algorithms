"""
DFS with Return Values (Path Problems)
Sometimes DFS returns info upwards (like sum of paths).
Example: Find max depth of a tree.

✅ Used in: “Maximum Depth of Binary Tree”, “Diameter of Binary Tree”.
"""

def max_depth(root):
    if not root:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return 1 + max(left, right)
