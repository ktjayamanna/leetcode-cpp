def dfs(node, target, path):
    """
    Performs a depth-first search on a binary tree to find a target node.
    Path is a stack that keeps track of the path from the root to the current node.

    Args:
        node: The current node to search.
        target: The target node to search for.
        path: The current path of nodes to this node. Path is implemented as a stack.

    Returns:
        A list of nodes from the root to the target node, or None if the target
        node is not found.
    """
    if not node:
        return None
    path.append(node)
    if node == target:
        return path[:]
    left_path = dfs(node.left, target, path)
    right_path = dfs(node.right, target, path)
    path.pop()  # Backtrack
    return left_path or right_path