import heapq

class Solution:

    def findKthLargest(self, nums, k):
        # Negate the elements to simulate a max-heap
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)  # Heapify the array
        
        # Pop the root of the heap k times
        kth_largest = None
        for _ in range(k):
            kth_largest = -heapq.heappop(max_heap)  # Remove the largest and revert the sign
        
        return kth_largest
        