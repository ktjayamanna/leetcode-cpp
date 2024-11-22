# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

from collections import deque

def breadth_first_values(root):
  queue = deque([root])
  values = []
  if not root:
    return values

  while True:
    curr = queue.popleft()
    values.append(curr.val)
    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)
    if len(queue) == 0:
      return values

    
    
    
  