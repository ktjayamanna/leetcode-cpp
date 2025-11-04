# Heap Insertion
# Implementing heap insertion operation

"""
PROBLEM DESCRIPTION:
================================================================================
Implement the insert method for the existing class. The method should properly add a given value into the heap, maintaining min heap order and height balance.

EXAMPLES:
================================================================================
heap = MinHeap()
heap.insert(12)
heap.insert(13)
heap.insert(11)
heap.insert(4)
heap.insert(20)
heap.insert(9)
heap.insert(22)
heap.insert(14)

#
#               4
#            /    \
#          11      9
#         / \    /  \
#       13  20  12  22
#      /
#    14
#
# [ 4, 11, 9, 13, 20, 12, 22, 14 ]

heap = MinHeap()
heap.insert(12)
heap.insert(93)
heap.insert(63)
heap.insert(16)
heap.insert(-500)
heap.insert(21)
heap.insert(11)
heap.insert(43)
heap.insert(-6)
heap.insert(35)
heap.insert(15)
heap.insert(37)
heap.insert(29)
heap.insert(-501)
heap.insert(80)

#                              -501
#                      /                \
#                    -6                -500
#                 /     \            /       \
#               12      15          29        11
#             /  \     /  \       /  \       /  \
#            93  43   35  16    63   37     21  80
#
#
# [ -501, -6, -500, 12, 15, 29, 11, 93, 43, 35, 16, 63, 37, 21, 80 ]


COMPLEXITY:
================================================================================
n = number of items in heap
Time: O(log(n))
Space: O(1)

"""

# SOLUTION:
# ================================================================================
'''
left = 2 x i + 1
right = 2 x i + 2
parent = floor(
(i - 1) / 2
)
root => i = 0
'''
'''
left = 2 x i + 1
right = 2 x i + 2
parent = floor(
(i - 1) / 2
)
root => i = 0
'''
import math

class MinHeap:
  def __init__(self):
    self.list = []
    
  def is_empty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)
      
  def insert(self, val):
    self.list.append(val)
    self.swift_up()

  def swift_up(self):
    i = len(self.list) - 1
    while i >= 0:
      parent = math.floor(
        (i - 1) / 2
      )
      if self.list[parent] > self.list[i]:
        self.list[parent], self.list[i] = self.list[i], self.list[parent]
        i = parent
      else:
        break

heap = MinHeap()
heap.insert(12)
heap.insert(13)
heap.insert(11)
heap.insert(4)
heap.insert(20)
heap.insert(9)
heap.insert(22)
heap.insert(14)

#
#               4
#            /    \
#          11      9
#         / \    /  \
#       13  20  12  22
#      /
#    14
#
# [ 4, 11, 9, 13, 20, 12, 22, 14 ]

    