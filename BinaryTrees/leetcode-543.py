#for a given tree: diameter = (1 + left sub tree height) + (1 + right sub tree height)
#find the diameter for every tree and update max_diameter
# How do we find the height? 
    #height = max(1 + left sub tree height, 1 + right sub tree height )
    #height = 0 for single node tree
    #height = -1 for empty tree

import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def _height(root):
            if not root:
                return -1
            
            left_tree = _height(root.left)
            right_tree = _height(root.right)
            diameter =  1 + left_tree + 1 + right_tree
            if self.max_diameter < diameter:
                self.max_diameter = diameter
            return 1 + max(left_tree, right_tree)
        _height(root)
        return self.max_diameter




        