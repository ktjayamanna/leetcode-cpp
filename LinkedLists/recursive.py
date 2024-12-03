class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def linked_list_values_pattern_1(head):
  if not head:
    return []
  next_node = linked_list_values_pattern_1(head.next)
  return [head.val] + next_node


def linked_list_values_pattern_2(head):
    result = []
    helper(head, result)
    return result

def helper(head, result):
    if not head:
      return None
    result.append(head.val)
    helper(head.next, result)

    
    
