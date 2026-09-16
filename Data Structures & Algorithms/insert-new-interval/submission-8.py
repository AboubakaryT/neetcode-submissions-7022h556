class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        """
        If newInterval[0] <= intervals[1] and newInterval[1] >= nextInterval[0] we combine the two.
        else we just 

        [[1,3],[6.7]] , newInterval = [2,5]
        [[1,5],[6,7]]
        if it's in both inte
        if it's in the left intervals -> combine with the left
        if it's in the right intervals -> combine with right
        if it's not in any interval -> append
        """
        n = len(intervals)
        res = []
        idx = 0
        start, end = newInterval[0], newInterval[1]

        while idx < n and start > intervals[idx][1]:
            res.append(intervals[idx])
            idx+=1
        #overlapping
        while idx < n and end >= intervals[idx][0]:
            start = min(intervals[idx][0], start)
            end = max(intervals[idx][1], end)
            idx+=1
        res.append([start,end])

        while idx < n and end <= intervals[idx][0]:
            res.append(intervals[idx])
            idx+=1

        return res
            
            

