# Lefty Nodes
# Find all leftmost nodes at each level of a binary tree

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, lefty_nodes, that takes in the root of a binary tree. The function should return a list containing the left-most value on every level of the tree. The list must be ordered in a top-down fashion where the root is the first item.

Note that the left-most node on a level may not necessarily be a left child.

EXAMPLES:
================================================================================
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

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

lefty_nodes(a) # [ 'a', 'b', 'd', 'g' ]

u = Node('u')
t = Node('t')
s = Node('s')
r = Node('r')
q = Node('q')
p = Node('p')

u.left = t
u.right = s
s.right = r
r.left = q
r.right = p

#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p

lefty_nodes(u) # [ 'u', 't', 'r', 'q' ]


COMPLEXITY:
================================================================================
n = number of nodes
Time: O(n)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# ---------------- DFS ----------------

def lefty_nodes(root):
  values = []
  traverse(root, 0, values)
  return values

def traverse(root, level, values):
  if root is None:
    return
  
  if len(values) == level:
    values.append(root.val)
    
  traverse(root.left, level + 1, values)
  traverse(root.right, level + 1, values) 


# ---------------- BFS ----------------

from collections import deque

def lefty_nodes(root):
  queue = deque([(root, 0)])
  result = []
  prev_level = None
  while queue:
    current, level = queue.popleft()
    if prev_level is None:
      prev_level = 0
      result.append(current.val)
    elif prev_level != level:
      result.append(current.val)
      prev_level = level
    if current.left:
      queue.append(
        (current.left, level + 1)
      )
    if current.right:
      queue.append(
        (current.right, level + 1)
      )
  return result


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

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

lefty_nodes(a) # [ 'a', 'b', 'd', 'g' ]

