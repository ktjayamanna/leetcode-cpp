# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
  if not root:
    return float("-inf")
  if not root.left and not root.right:
    return root.val
  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))
    
'''
#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

In this problem, challenge is to handle the null nodes.
There are two kinds of null nodes:
1. Null nodes that are sibling to valid nodes.
2. Null nodes that are children of leaf nodes.

In our design, 1 is handled by,  
if not root:
    return float("-inf")

In our design, 2 is handled by,
if not root.left and not root.right:
    return root.val
'''