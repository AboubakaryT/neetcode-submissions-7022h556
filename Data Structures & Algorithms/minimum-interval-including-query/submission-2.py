import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minHeap = []
        i = 0
        intervals.sort()
        #index, queries
        newQ = [(i, queries[i]) for i in range(len(queries))] 
        #sort by query value
        newQ.sort(key=lambda x: x[1])
        for index, val in newQ:
            while i < len(intervals) and val >= intervals[i][0]:
                start, end = intervals[i]
                if start <= val <= end:
                    heapq.heappush(minHeap, (end-start + 1, end))
                i+=1
            while minHeap and minHeap[0][1] < val:
                heapq.heappop(minHeap)
            queries[index] = minHeap[0][0] if minHeap else -1


        return queries