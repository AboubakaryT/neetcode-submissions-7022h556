class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        6,4,3,2,2
        3,2,2,2
        2,2,1
        
        """
        maxHeap = [-x for x in stones]
        #[7,3,2]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first = -heapq.heappop(maxHeap)
            second = -heapq.heappop(maxHeap)
            new = first - second
            
            if new >= 0:
                heapq.heappush(maxHeap,-new)
            print(maxHeap)

        return -maxHeap[0]

            


