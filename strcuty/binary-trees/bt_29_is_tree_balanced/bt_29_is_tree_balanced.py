# Is Tree Balanced
# Check if a binary tree is balanced

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, is_tree_balanced, that takes in the root of a binary tree. 
The function should return a boolean indicating whether or not the tree is "balanced".

A "balanced" binary tree is a binary tree where the height between the left and right subtrees differs by at most 1 for every node.

EXAMPLES:
================================================================================
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.left = b
a.right = c
b.right = d

#         a
#       /   \
#      b    c
#      \
#      d

is_tree_balanced(a) # -> True

a = Node("a")
b = Node("b")
c = Node("c")

a.right = b
b.right = c

#        a
#         \
#          b
#          \
#           c

is_tree_balanced(a) # -> False


COMPLEXITY:
================================================================================
n = number of nodes
Time: O(n)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
def check_height_balance(root):
    if root is None:
        return 0

    left_height = check_height_balance(root.left)
    if left_height == -1:
        return -1

    right_height = check_height_balance(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1
    else:
        return 1 + max(left_height, right_height)

def is_tree_balanced(root):
    return check_height_balance(root) > -1
# My answer which is more aligned with the definition of the height of a tree.
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def _is_tree_balanced(root):
  if not root:
    return -1
  left = _is_tree_balanced(root.left)
  right = _is_tree_balanced(root.right)
  if abs(left - right) > 1:
    return float('inf')
  else:
    return 1 + max(left, right)

def is_tree_balanced(root):
  return False if _is_tree_balanced(root) == float('inf') else True

    
