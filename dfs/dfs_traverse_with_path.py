# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
    def dfs(node, path):
        if not node:
            return []
        path.append(node.val)
        
        if not node.left and not node.right:
            # At a leaf node, directly return a copy of the current path
            leaf_path = [path[:]]
            path.pop()
            return leaf_path
        
        # Recursively get paths from left and right subtrees
        left_paths = dfs(node.left, path)
        right_paths = dfs(node.right, path)
        
        # Backtrack after exploring both subtrees
        path.pop()
        
        # Directly return the combined paths without a separate result variable
        return left_paths + right_paths
    
    return dfs(root, [])


def get_path(root, val):
  """
  Gets the path from the root to a node with the given value, or None if not found.

  Args:
    root: The root of the binary tree.
    val: The value of the node to search for.

  Returns:
    None if the node is not found, otherwise a list of node values from the root to
    the node.
  """
  
  if not root: return None
  if root.val == val: return [root.val]
  left = get_path(root.left, val)
  if left: return left + [root.val]
  right = get_path(root.right, val)
  if right: return right + [root.val]
  return None
  



  