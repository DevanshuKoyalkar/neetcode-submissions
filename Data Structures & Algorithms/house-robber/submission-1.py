class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        select, dont_select = 0, 0

        for i in range(n):
            select, dont_select = dont_select+nums[i], max(select,dont_select)
            result = max(select, dont_select)
        return result

        
