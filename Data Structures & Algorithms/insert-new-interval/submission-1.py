class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        # intervals.sort()
        
        # [prev_start, prev_end] = intervals[0]

        # result = []

        # for i in range(1, len(intervals)):

        #     [start, end] = intervals[i]

        #     if start > prev_end:
        #         result.append([prev_start, prev_end])
        #         prev_start, prev_end = start, end
            
        #     else:
        #         prev_end = max(prev_end, end)
        
        # result.append([prev_start, prev_end])

        # return result


        ## SECOND APPROACH
        result = []
        new_start, new_end = newInterval

        for start, end in intervals:
            if new_start > end:
                result.append([start, end])
            
            elif start > new_end:
                result.append([new_start, new_end])
                new_start, new_end = start, end
            
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
        
        result.append([new_start, new_end])
        return result
