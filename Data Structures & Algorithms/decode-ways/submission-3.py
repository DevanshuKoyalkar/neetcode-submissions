class Solution:
    def numDecodings(self, s: str) -> int:
        # LEN = len(s)

        
        # dp = [0] * (LEN + 1)

        # dp[0] = 1
        # dp[1] = 0 if s[0] == '0' else 1

        # # dp[k] means decoding first k characters
        # for pos in range(2, LEN+1):
        #     ch = s[pos - 1]
        #     ch_prev = s[pos - 2]

            
        #     if ch != '0':
        #         dp[pos] += dp[pos-1] 
        #     if ch_prev == '1' or (ch_prev == '2' and ch in '0123456'):
        #         dp[pos] += dp[pos-2]
        
        # return dp[LEN]

        # SECOND TRY

        LEN = len(s)

        ways_to_second_last = 1
        ways_to_last = 0 if s[0] == '0' else 1

        # dp[k] means decoding first k characters
        for pos in range(2, LEN+1):
            current_char = s[pos - 1]
            previous_char = s[pos - 2]

            ways_to_current = 0
            if current_char != '0':
                ways_to_current += ways_to_last
            if previous_char == '1' or (previous_char == '2' and current_char in '0123456'):
                ways_to_current += ways_to_second_last

            ways_to_second_last = ways_to_last
            ways_to_last = ways_to_current

        return ways_to_last

            
