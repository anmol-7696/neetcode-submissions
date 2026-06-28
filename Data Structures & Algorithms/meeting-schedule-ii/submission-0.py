"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0 
        
        rooms = 1

        intervals.sort(key = lambda x:x.end)
        end = intervals[0].end
        
        for i in range(1,len(intervals)):
            if intervals[i].start < end:
                rooms += 1
            else:
                end = max(end, intervals[i].end)
        return rooms 


