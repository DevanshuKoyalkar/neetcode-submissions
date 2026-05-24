class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # greedy --> if there are multiple overlappign intervals we should always keep the interval which ends first in order to avoid further conflicts

        intervals.sort()

        prev_start, prev_end = intervals[0]
        counter = 0

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start >= prev_end:
                prev_start, prev_end = start, end
            else:
                # overlap choose min end
                prev_end = min(prev_end, end)
                counter += 1
        
        return counter