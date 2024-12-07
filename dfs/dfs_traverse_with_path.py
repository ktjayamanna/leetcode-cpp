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



  