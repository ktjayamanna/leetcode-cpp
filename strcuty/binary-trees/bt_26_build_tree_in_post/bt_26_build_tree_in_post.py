# Build Tree In Post
# Build a binary tree from inorder and postorder traversals

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, build_tree_in_post, that takes in a list of in-ordered values and a list of post-ordered values for a binary tree. 
The function should build a binary tree that has the given in-order and post-order traversal structure. 
The function should return the root of this tree.

You can assume that the values of inorder and postorder are unique.

EXAMPLES:
================================================================================

build_tree_in_post(
  [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
  [ 'd', 'g', 'h', 'e', 'b', 'f', 'c', 'a' ] 
)
#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

build_tree_in_post(
  [ 'd', 'b', 'e', 'a', 'f', 'c', 'g' ],
  [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 
)
#      a
#    /    \
#   b      c
#  / \    / \
# d   e  f   g


COMPLEXITY:
================================================================================
n = length of array
Time: O(n^2)
Space: O(n^2)

"""

# SOLUTION:
# ================================================================================
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def build_tree_in_post(in_order, post_order):
  if len(in_order) == 0:
    return None
  
  value = post_order[-1]
  root = Node(value)
  mid = in_order.index(value)
  left_in = in_order[:mid]
  right_in = in_order[mid + 1:]  
  left_post = post_order[:len(left_in)]
  right_post = post_order[len(left_in):-1]
  root.left = build_tree_in_post(left_in, left_post)
  root.right = build_tree_in_post(right_in, right_post)
  return root

