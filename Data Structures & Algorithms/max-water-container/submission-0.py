class Solution:
    def maxArea(self, heights: List[int]) -> int:
        LEN = len(heights)

        start = 0
        end = LEN - 1

        max_area = 0


        while start < end:
            current_area = (end - start) * min(heights[start], heights[end])
            max_area = max(max_area, current_area)

            if heights[start] >= heights[end]:
                end -= 1
            else:
                start += 1
        
        return max_area
