"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        n = len(intervals)

        if n == 0: return True

        prev_end = intervals[0].end

        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end

            if start < prev_end:
                return False
            
            prev_end = end
        
        return True