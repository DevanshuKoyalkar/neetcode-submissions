class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        
        [prev_start, prev_end] = intervals[0]

        result = []

        for i in range(1, len(intervals)):

            [start, end] = intervals[i]

            if start > prev_end:
                result.append([prev_start, prev_end])
                prev_start, prev_end = start, end
            
            else:
                prev_end = max(prev_end, end)
        
        result.append([prev_start, prev_end])

        return result