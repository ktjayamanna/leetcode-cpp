def reverse_list(head, prev=None):
  if not head:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)