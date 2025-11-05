# Heap Deletion
# Implementing heap deletion operation

"""
PROBLEM DESCRIPTION:
================================================================================
Implement the extract_min method for the existing class. The method should return and remove the smallest value in the heap, maintaining min heap order and height balance.

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
heap1.extract_min() # -> 4
heap1.extract_min() # -> 9
heap1.extract_min() # -> 11

heap = MinHeap()
heap.insert(12)
heap.insert(93)
heap.insert(63)
heap.insert(16)
heap.extract_min() # -> 12
heap.extract_min() # -> 16
heap.insert(-500)
heap.insert(21)
heap.insert(11)
heap.insert(43)
heap.insert(-6)
heap.insert(35)
heap.insert(15)
heap.extract_min() # -> -500
heap.extract_min() # -> -6
heap.extract_min() # -> 11
heap.extract_min() # -> 15
heap.extract_min() # -> 21
heap.extract_min() # -> 35
heap.extract_min() # -> 43
heap.extract_min() # -> 63
heap.extract_min() # -> 93


COMPLEXITY:
================================================================================
n = number of items in heap
Time: O(log(n))
Space: O(1)

"""

# SOLUTION:
# ================================================================================
class MinHeap:
  def __init__(self):
    self.list = []
    
  def is_empty(self):
    return len(self.list) == 0

  def size(self):
    return len(self.list)
  
  def swap(self, index_1, index_2):
    self.list[index_1], self.list[index_2] = self.list[index_2], self.list[index_1]
  
  def sift_up(self, index):
    current_index = index
    while current_index > 0:
      parent_index = (current_index - 1) // 2
      if self.list[current_index] < self.list[parent_index]:
        self.swap(current_index, parent_index)
        current_index = parent_index
      else:
        break
    
  def insert(self, val):
    self.list.append(val)
    self.sift_up(self.size() - 1)
      
  def extract_min(self):
    if self.is_empty(): return None
    if self.size() == 1: return self.list.pop()
    root = self.list[0]
    self.list[0] = self.list.pop()
    self.sift_down(0)
    return root

  def sift_down(self, index):
    current_index = index
    while current_index < self.size() - 1:
      left_idx = 2 * current_index + 1
      right_idx = 2 * current_index + 2
      left_val = self.list[left_idx] if left_idx < self.size() else float('inf')
      right_val = self.list[right_idx] if right_idx < self.size() else float('inf')
      smaller_child_val = left_val if left_val < right_val else right_val
      smaller_child_idx = left_idx if left_val < right_val else right_idx
      if self.list[current_index] > smaller_child_val:
        self.swap(current_index, smaller_child_idx)
        current_index = smaller_child_idx
      else:
        break
      
    
    

