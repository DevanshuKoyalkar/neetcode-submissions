class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        SUM = sum(nums)

        if SUM % 2 == 1: return False
        target = SUM // 2

        dp = [True] + [False] * target

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]
        
            if dp[target]:
                return True
        
        return dp[target]

