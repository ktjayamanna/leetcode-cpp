# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
    """
    Performs a pre-order (root, left, right) depth-first traversal of a binary tree.

    Args:
        root (Node): The root node of the binary tree.

    Returns:
        list: A list of values obtained from a depth-first traversal of the tree.
    """
    if not root:
        return []
    stack, values = [root], []
    while stack:
        current = stack.pop()
        values.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return values

    
    
    
