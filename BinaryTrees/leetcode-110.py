# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True

        def height(root):
            if not root:
                return -1
            left = height(root.left)
            right = height(root.right)
            gap = abs(left - right) > 1
            if gap == True:
                self.is_balanced = False
            return 1 + max(left, right)
        
        height(root)
        return self.is_balanced
        