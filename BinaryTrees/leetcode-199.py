# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
from collections import deque
from typing import List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                curr = queue.popleft()
                # Enqueue left and right children of the current node
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                # If this is the last node at the current level, add its value to res
                if i == level_size - 1:
                    res.append(curr.val)
        return res
        