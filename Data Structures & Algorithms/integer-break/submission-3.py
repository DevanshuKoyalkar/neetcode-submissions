class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 5)

        dp[0] = 0 # can't break it 
        dp[1] = 0 # can't break it
        dp[2] = 1

        for i in range(3, n + 1):
            for j in range(1, i): # j has to be less than i
                dp[i] = max([dp[i], dp[i-j] * j, (i-j) * j])

        return dp[n]
