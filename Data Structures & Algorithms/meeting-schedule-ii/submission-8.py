"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #[1,1,2,5,10,15]
        #[5,6,10,15,20,20]
        #meetings = 2
        #s= 5
        #e = 3
        start = []
        end = []
        meetings = 0
        s = 0
        e = 0
        res = 0
        for i in intervals:
            start.append(i.start)
            end.append(i.end)

        start.sort()
        end.sort()
        
        while s < len(intervals):
            if start[s] < end[e]:
                s+=1
                meetings+=1
            else:
                e+=1
                meetings-=1
            res = max(res,meetings)
        return res
            


       
       

