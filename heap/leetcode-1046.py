import heapq

class Solution:
    def lastStoneWeight(self, stones):
        max_heap = [-num for num in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Pop two largest elements
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            z = y - x

            # If z > 0, push it back into the heap
            if z > 0:
                heapq.heappush(max_heap, -z)

        # Return the final element if the heap is not empty, otherwise return 0
        return -max_heap[0] if max_heap else 0


        
