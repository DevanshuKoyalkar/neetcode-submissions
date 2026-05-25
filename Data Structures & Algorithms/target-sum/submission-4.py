class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        LEN = len(nums)

        dp = {0: 1}

        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp = next_dp
        
        return dp[target]

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        LEN = len(nums)

        dp = [defaultdict(int) for _ in range(LEN + 1)]
        dp[0] = {0: 1}

        for i in range(LEN):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        
        return dp[LEN][target]

        

        

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
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