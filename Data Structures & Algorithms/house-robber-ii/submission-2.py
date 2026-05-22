class Solution:
    

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        def rob_linear(start, end):
            result = 0
            select, dont_select = 0, 0

            for i in range(start, end):
                select, dont_select = dont_select+nums[i], max(select,dont_select)
            return max(select, dont_select)


        return max(rob_linear(1, n), rob_linear(0,n-1))
    