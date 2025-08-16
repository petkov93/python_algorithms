def level_order(root):
    """
    Classic binary tree BFS — processes nodes by depth.
    """
    if not root: return []
    from collections import deque
    queue = deque([root])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result

"""
✅ Used in: “Binary Tree Level Order Traversal”, “Right Side View”.
"""