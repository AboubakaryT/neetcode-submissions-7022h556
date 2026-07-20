from _heapq import heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-x for x in nums]
        maxHeap = nums
        heapq.heapify(maxHeap)
        i = 0
        while i < k :
            pop = heapq.heappop(maxHeap)
            i+=1
            if i == k:
                return -pop