# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Helper function to perform DFS and return the path
        def dfs(node, target, path):
            if not node:
                return None
            path.append(node)
            if node == target:
                return path[:]
            left_path = dfs(node.left, target, path)
            right_path = dfs(node.right, target, path)
            path.pop()  # Backtrack
            return left_path or right_path

        # Get paths for p and q
        p_path = dfs(root, p, [])
        q_path = dfs(root, q, [])

        # Find the earliest common node in both paths
        i = 0
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            i += 1
        return p_path[i - 1] if i > 0 else None

        return None


# More optimal answer
""" 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: If the root is None, or if the root matches either p or q
        if not root or root == p or root == q:
            return root

        # Recursively search for p and q in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are not None, root is the LCA
        if left and right:
            return root

        # Otherwise, return the non-None result
        return left if left else right 
        """
