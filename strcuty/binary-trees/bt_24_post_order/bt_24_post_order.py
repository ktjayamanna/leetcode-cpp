# Post Order
# Traverse a binary tree in post-order

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, post_order, that takes in the root of a binary tree. 
The function should return a list containing the post-ordered values of the tree.
Post-order traversal is when nodes are recursively visited in the order: left child, right child, self.

EXAMPLES:
================================================================================
x = Node('x')
y = Node('y')
z = Node('z')

x.left = y
x.right = z

#       x
#    /    \
#   y      z

post_order(x)
# ['y', 'z', 'x']

l = Node('l')
m = Node('m')
n = Node('n')
o = Node('o')
p = Node('p')
q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')

l.left = m
l.right = n
n.left = o
n.right = p
o.left = q
o.right = r
p.left = s
p.right = t

#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t

post_order(l)
# [ 'm', 'q', 'r', 'o', 's', 't', 'p', 'n', 'l' ] 


COMPLEXITY:
================================================================================
n = number of nodes
Time: O(n)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
def post_order(root):
  values = []
  post_order_traversal(root, values)
  return values

def post_order_traversal(root, values):
  if root is None:
    return 
  post_order_traversal(root.left, values)
  post_order_traversal(root.right, values)
  values.append(root.val)

