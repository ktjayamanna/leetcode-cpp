# Linked List Cycle
# Detect if linked list has a cycle

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, linked_list_cycle, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains a cycle.

EXAMPLES:
================================================================================
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.next = b
b.next = c
c.next = d
d.next = b # cycle

#         _______
#       /        \
# a -> b -> c -> d 

linked_list_cycle(a)  # True


COMPLEXITY:
================================================================================

n = number of nodes
Time: O(n)
Space: O(1)
"""

# SOLUTION:
# ================================================================================

def linked_list_cycle(head):
  first_iteration = True
  
  fast = head
  slow = head
  while fast is not None and fast.next is not None:
    if slow is fast and not first_iteration:
      return True
    first_iteration = False
    slow = slow.next
    fast = fast.next.next
    
  return False
