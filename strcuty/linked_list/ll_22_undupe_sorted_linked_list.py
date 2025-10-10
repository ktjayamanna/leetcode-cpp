# Undupe Sorted Linked List
# Remove duplicates from sorted linked list

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function that takes in a linked list that contains values in increasing order.
The function should return a new linked list containing the original values, with duplicates removed. 
The relative order of values in the resulting linked list should be unchanged.

EXAMPLES:
================================================================================

a = Node(4)
b = Node(4)
c = Node(6)
d = Node(6)
e = Node(6)
f = Node(7)
g = Node(7)

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
f.next = g;

# 4 -> 4 -> 6 -> 6 -> 6 -> 7 -> 7

undupe_sorted_linked_list(a) # 4 -> 6 -> 7


a = Node(4)
b = Node(4)
c = Node(6)
d = Node(6)
e = Node(6)
f = Node(7)
g = Node(7)

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
f.next = g;

# 4 -> 4 -> 6 -> 6 -> 6 -> 7 -> 7

undupe_sorted_linked_list(a) # 4 -> 6 -> 7



COMPLEXITY:
================================================================================
n = number of nodes
Time: O(n)
Space: O(n)

"""

# SOLUTION:
# ================================================================================
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def undupe_sorted_linked_list(head):
  dummy_head = Node(None);
  tail = dummy_head
  
  current = head
  while current is not None:
    if current.val != tail.val:
      tail.next = Node(current.val)
      tail = tail.next
    current = current.next
  return dummy_head.next

