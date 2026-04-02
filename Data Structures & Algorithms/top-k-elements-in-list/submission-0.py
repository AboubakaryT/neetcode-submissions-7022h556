import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, value in counter.items():
                           #2 
            if len(heap) < k:
                ##we only want to store K elements so that we can return this.
                heapq.heappush(heap,(value,key))
                print(heap)
            else:
                #adds the next element, than removes what is smallest of k elements
                heapq.heappushpop(heap, (value, key))
                print(heap)
        nums = []

        for h in heap:
            nums.append(h[1])
        return nums
        # return [h[1] for h in heap]
                 
