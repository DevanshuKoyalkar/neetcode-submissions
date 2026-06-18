class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        dp = [0] * (target + 1)

        dp[0] = 1 # we can alway reach 0

        # [1 0 0 0 0]
        # [1,2,3]

        # 1 --> [1, 1, 1, 1, 1]
        # 2 --> [1, 1, 2, 2, 3]
        # form 2 --> 1,1 or 2 --> 2 ways
        # form 3 --> 1,1,1 or 1,2 --> 2 ways
        # form 4 --> 1,1,1,1 or 1,1,2 or 2,2 

        # THIS IS COMBINATIONS
        # for num in nums:
        #     for i in range(1, target + 1):
        #         if i >= num: 
        #             dp[i] += dp[i-num]

        # THIS I PERMUTATIONS
        for i in range(1, target + 1):
            for num in nums:
                if i >= num: 
                    dp[i] += dp[i-num]
        
        return dp[target]
