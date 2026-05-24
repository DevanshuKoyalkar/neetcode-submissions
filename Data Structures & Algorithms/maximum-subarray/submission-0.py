class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, interval_sum = float('-inf'), 0

        start, end = 0, 0


        while end < len(nums):
            interval_sum += nums[end]

            max_sum = max(max_sum, interval_sum)
            print(start, end, interval_sum, max_sum)

            if interval_sum <= 0:
                start = end = end + 1
                interval_sum = 0
            else:
                end += 1
        
        return max_sum