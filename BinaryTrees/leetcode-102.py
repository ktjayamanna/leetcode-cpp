from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Return an empty list if the root is None

        queue = deque([root])  # Initialize the queue with the root node
        result = []  # List to store the values level by level
        level_size = len(queue)  # Number of nodes at the current level


        while queue:
            current_level = []  # List to store the current level's values

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)  # Add the current node's value

                # Add the current node's children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_size = len(queue)  # Number of nodes at the current level is updated as soon as previous layer is done.
            result.append(current_level)  # Add the current level to the result

        return result


        