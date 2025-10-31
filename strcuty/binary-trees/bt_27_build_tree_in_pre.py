class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def build_tree_in_pre(in_order, pre_order):
  print(" In order: " , in_order , " Pre order: " , pre_order)
  if not in_order:
    return None
  root = Node(pre_order[0])
  split = in_order.index(root.val)
  root.left = build_tree_in_pre(
    in_order[0 : split],
    pre_order[1: split + 1]
  )
  root.right = build_tree_in_pre(
    in_order[split + 1:],
    pre_order[split + 2:]
  )
  return root


build_tree_in_pre(
  [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
  [ 'a', 'b', 'd', 'e', 'g', 'h', 'c', 'f' ] 
)
#       a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h

  
  