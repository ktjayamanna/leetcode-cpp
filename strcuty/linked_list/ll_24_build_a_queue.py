# Build a Queue
# Implement queue using linked list

"""
PROBLEM DESCRIPTION:
================================================================================
Implement the enqueue and dequeue methods for the existing class. 
The enqueue method should add a given value into the queue. 
The dequeue should return and remove an item from the queue following first-in, first-out order.

Your implementation should use a linked-list and not any built in containers.

EXAMPLES:
================================================================================
queue = Queue()
queue.enqueue("a")
queue.size # -> 1
queue.dequeue() # -> a
queue.enqueue("b")
queue.enqueue("c")
queue.size # -> 2
queue.dequeue() # -> b
queue.dequeue() # -> c
queue.size # -> 0


queue = Queue()
queue.enqueue("a")
queue.enqueue("b")
queue.enqueue("c")
queue.dequeue() # -> a
queue.enqueue("d")
queue.enqueue("e")
queue.size # -> 4
queue.dequeue() # -> b
queue.dequeue() # -> c
queue.dequeue() # -> d
queue.dequeue() # -> e
queue.enqueue("x")
queue.enqueue("y")
queue.size # -> 2
queue.dequeue() # -> x
queue.dequeue() # -> y


COMPLEXITY:
================================================================================
n = number of items currently on the Queue
Total Queue Space: O(n)
enqueue
Time: O(1)
Space: O(1)
dequeue
Time: O(1)
Space: O(1)

"""

# SOLUTION:
# ================================================================================
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0
    
  def enqueue(self, val):
    if self.size == 0:
      self.head = Node(val)
      self.tail = self.head
    else:
      self.tail.next = Node(val)
      self.tail = self.tail.next
    self.size += 1
    
  def dequeue(self):
    if self.size == 0:
      return None
    
    value = self.head.val
    
    if self.size == 1:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.next
    
    self.size -= 1
    return value

