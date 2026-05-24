class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]

        ROWS, COLS = m, n

        dp = [0] * COLS

        dp[0] = 1
        for _ in range(ROWS):
            for i in range(1, COLS):
                dp[i] += dp[i-1]
            
            # print(dp)

        
        return dp[COLS-1]
        
