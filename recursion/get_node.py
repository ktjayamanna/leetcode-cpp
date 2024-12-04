def get_node_value(head, index): 
  if not head:
    return None
  if index == 0:
    return head.val

  return get_node_value(head.next, index -1)




# Iterative version for contextdef get_node_value(head, index):
def get_node_value(head, index):
  current = head
  count = 0
  while current:
    if count == index:
      return current.val
    count +=1
    current = current.next
  return None