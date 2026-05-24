"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [(interval.start,1) for interval in intervals]
        ends = [(interval.end,0) for interval in intervals]

        borders = starts + ends
        borders.sort(key = lambda x:(x[0], x[1]))

        count = 0
        max_count = 0

        for border, is_start in borders:
            if is_start:
                count += 1
            else:
                count -= 1
            
            max_count = max(max_count, count)
        
        return max_count
            