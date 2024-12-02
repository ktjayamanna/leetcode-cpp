import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Initialize a min-heap with up to k elements
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        
        # Reduce the heap size to k if necessary
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Add the new value only if it can be in the top k elements
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        
        # Return the kth largest element, which is the root of the heap
        return self.min_heap[0]
