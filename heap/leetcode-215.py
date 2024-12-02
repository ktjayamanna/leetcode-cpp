import heapq

class Solution:

    # Heapify all n elements with a max heap.
    # def findKthLargest(self, nums, k):
    #     # Negate the elements to simulate a max-heap
    #     max_heap = [-num for num in nums]
    #     heapq.heapify(max_heap)  # Heapify the array
        
    #     # Pop the root of the heap k times
    #     kth_largest = None
    #     for _ in range(k):
    #         kth_largest = -heapq.heappop(max_heap)  # Remove the largest and revert the sign
        
    #     return kth_largest
        
    # Heapify only k elements at a time with min heap
    def findKthLargest(self, nums, k):
        # Step 1: Build a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # O(k)
        
        # Step 2: Process the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:
                # Replace root and heapify; O(log k)
                heapq.heapreplace(min_heap, num)
        
        # Step 3: The root is the k-th largest element
        return min_heap[0]