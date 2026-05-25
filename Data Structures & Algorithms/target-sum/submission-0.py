class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        LEN = len(nums)
        nums.sort()

        SUM = sum(nums)
        MAX, MIN = -SUM, SUM
        memo = {}
        # order doesn't matter here
        # each position two choices positive or negative, explore all is 2^n
        
        # how manys ways to reach subset_sum from pos
        def helper(pos, subset_sum):
            if (pos, subset_sum) in memo:
                return memo[(pos, subset_sum)]

            if pos == LEN:
                res = 1 if subset_sum == 0 else 0
                memo[(pos, subset_sum)] = res
                return res
            
            res =  helper(pos + 1, subset_sum + nums[pos]) + helper(pos + 1, subset_sum - nums[pos])
            memo[(pos, subset_sum)] = res
            return res
            
        return helper(0, target)