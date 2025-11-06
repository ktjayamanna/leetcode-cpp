# Kth Largest
# Finding the kth largest element in a collection

"""
PROBLEM DESCRIPTION:
================================================================================
Write a function, kth_largest, that takes in a list of numbers and a value, k. 
The function should return the k-th largest element of the list.

EXAMPLES:
================================================================================
kth_largest([9,2,6,6,1,5,8,7], 3) # -> 7

numbers = [  
  4,5,85,77,47,80,37,42,3,6,62,33,69,68,16,20,83,39,14,58,75,35,72,36,19,18,66,61,41,79,28,43,7,24,40,53,32,12
]
kth_largest(numbers, 9) # -> 68

COMPLEXITY:
================================================================================
n = length of list
k = k-value
Time: O(n*log(k))
Space: O(k)

"""

# SOLUTION:
# ================================================================================
import heapq

def kth_largest(numbers, k):
  heap = []
  for num in numbers:
    heapq.heappush(heap, num)
    if len(heap) > k:
      heapq.heappop(heap)
  return heapq.heappop(heap)


