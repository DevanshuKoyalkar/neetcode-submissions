class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # cat crabt

        # dp[i][j] == lcs(first i chars of text1 and first j chars of text2)

        # bottom up dp 
        #       if text1[i]==text2[j]: dp[i][j] = 1 + dp[i-1][j-1]
        #        else: dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        ROWS, COLS = len(text1), len(text2)

        dp = [[0] * (COLS+1) for _ in range(ROWS+1)]

        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        # for row in dp:
        #     print(row)

        return dp[ROWS][COLS]