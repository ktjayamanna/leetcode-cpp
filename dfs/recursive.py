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

    left_tree = depth_first_values(root.left)
    right_tree = depth_first_values(root.right)

    return [root.val] + left_tree + right_tree

    
    
    
