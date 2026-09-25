class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #O(n log n )
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        #[1,2][1,4][2,4]
        #intervals=[[0,2],[1,3],[2,4],[3,5],[4,6]]
        for start,end in intervals[1:]:
            if start < prevEnd:
                res+=1
                prevEnd = min(end,prevEnd)
            else:
                prevEnd = max(end,prevEnd)
        return res

        
