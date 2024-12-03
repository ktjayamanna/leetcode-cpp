def linked_list_values(head):
  result = []
  while head:
    result.append(head.val)
    head = head.next
  return result