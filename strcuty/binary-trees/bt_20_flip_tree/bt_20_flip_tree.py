# Flip Tree
# Flip a binary tree horizontally (mirror image)

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, flip_tree, that takes in the root of a binary tree. 
The function should flip the binary tree, turning left subtrees into right subtrees and vice-versa. 
This flipping should occur in-place by modifying the original tree. 
The function should return the root of the tree.

EXAMPLES:
================================================================================
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#      a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

flip_tree(a) 

#       a
#    /    \
#   c      b
#  /     /   \
# f     e    d
#     /  \
#    h    g


COMPLEXITY:
================================================================================
n = number of nodes
Time: O(n)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
def flip_tree(root):
  if root is None:
    return None
  left = flip_tree(root.left)
  right = flip_tree(root.right)  
  root.left = right
  root.right = left
  return root

