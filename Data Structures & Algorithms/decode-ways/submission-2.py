class Solution:
    def numDecodings(self, s: str) -> int:
        LEN = len(s)

        
        dp = [0] * (LEN + 1)

        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        # dp[k] means decoding first k characters
        for pos in range(2, LEN+1):
            ch = s[pos - 1]
            ch_prev = s[pos - 2]

            
            if ch != '0':
                dp[pos] += dp[pos-1] 
            if ch_prev == '1' or (ch_prev == '2' and ch in '0123456'):
                dp[pos] += dp[pos-2]
        
        return dp[LEN]

            
