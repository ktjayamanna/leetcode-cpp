import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = [i for i in nums]
        heapq.heapify(self.min_heap)
        self.results = [None]
        #initialize the heap
        while True:
            if len(self.min_heap) == k:
                break
            if len(self.min_heap) > 0:
                heapq.heappop(self.min_heap)


    def add(self, val: int) -> int:
        if self.min_heap[0]<val:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        self.results.append(self.min_heap[0])
        return self.min_heap[0]
