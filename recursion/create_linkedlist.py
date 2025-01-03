class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# Iterative version
# def create_linked_list(values):
#   dummy = Node(-1)
#   current = dummy
#   for value in values:
#     current.next =  Node(value)
#     current = current.next
#   return dummy.next

# Recursive version
# def create_linked_list(values):
#   if len(values) == 0:
#     return None
#   current = Node(values[0])
#   current.next = create_linked_list(values[1:])
#   return current

# More optimized Recursive version
def create_linked_list(values, i = 0):
  if len(values) == i: #check if out of bounds
    return None 
  current = Node(values[i])
  current.next = create_linked_list(values, i + 1)
  return current