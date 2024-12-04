# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# Iterative version
# def is_univalue_list(head):
#   val = head.val
#   while head:
#     if val != head.val:
#       return False
#     head = head.next
#   return True

# Recursive version

def is_univalue_list(head):
    val = head.val
    return helper(head, val)

def helper(head, val):
    if not head:  # Base case: reached the end of the list
        return True
    if head.val != val:  # Early termination: mismatch found
        return False
    return helper(head.next, val)  # Continue recursion
