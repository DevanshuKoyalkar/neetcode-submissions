class Solution:
    def rob_linear(self, nums):
        n = len(nums)
        result = 0

        select, dont_select = 0, 0

        for i in range(n):
            select, dont_select = dont_select+nums[i], max(select,dont_select)
            result = max(select, dont_select)
        return result

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]


        return max(self.rob_linear(nums[1:]), self.rob_linear(nums[:-1]))
    