# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def remove_node(head, target_val):
#   prev = None
#   current = head
  
#   # handle head removal
#   if head.val == target_val:
#     return head.next
    
#   while current:
#     if current.val == target_val:
#       prev.next = current.next
#       return head
#     prev = current
#     current = current.next
#   return head

def remove_node(head, target_val):
  if not head:
    return None #nothing found so return the typical empty Node
  if head.val == target_val:
    return head.next
  head.next = remove_node(head.next, target_val)
  return head