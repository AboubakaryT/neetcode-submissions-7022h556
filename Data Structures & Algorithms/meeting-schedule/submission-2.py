"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)
        if intervals:
            start = [intervals[0].start, intervals[0].end]

        for i in range(1,len(intervals)):
            if start[0] > intervals[i].start or start[1] > intervals[i].start:
                return False

            start = [intervals[i].start, intervals[i].end]

        return True
