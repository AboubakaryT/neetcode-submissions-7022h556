class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #[1,3][1,5],[2,7]
        #[1,7] 
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            if lastEnd >= start:
                res[-1][1] = max(end,lastEnd)
            else: 
                res.append([start,end])

        return res 
             
            
        

      
