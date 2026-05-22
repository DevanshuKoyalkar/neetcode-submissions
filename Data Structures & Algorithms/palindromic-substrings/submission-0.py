class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        # bottom up dp, dp[i][j] tells if s[i:j] is a palindrome
        dp = [[0] * n for _ in range(n)]

        counter = 0

        for size in range(1, n + 1):
            for start in range(n - size + 1):
                end = start + size - 1
                if size == 1:
                    dp[start][end] = 1
                elif size == 2:
                    if s[start] == s[end]:
                        dp[start][end] = 1
                else:
                    if s[start] == s[end]:
                        dp[start][end] = dp[start+1][end-1]

                if dp[start][end] == 1:
                    counter += 1


        return counter