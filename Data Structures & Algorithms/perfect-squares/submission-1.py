class Solution:
    # 1 2 3 4 5 6 7 8 9
    # 1 2 3 1 2 
    def numSquares(self, n: int) -> int:
        if math.sqrt(n).is_integer():
            return 1

        dp = [0] * (n + 1)
        perfect_squares = set()
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            if math.sqrt(i).is_integer():
                dp[i] = 1
                perfect_squares.add(i)
                continue
            
            # using 1
            dp[i] = dp[i-1] + 1

            # using other squares
            for sq in perfect_squares:
                if i - sq >= 0:
                    dp[i] = min(dp[i-sq] + 1, dp[i])
        
        # print(dp)
        return dp[n]
