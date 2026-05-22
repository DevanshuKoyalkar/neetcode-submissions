class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        prev = 1
        prev_prev = 1

        for i in range(2, n + 1):
            res = prev + prev_prev
            prev_prev = prev
            prev = res
        
        return res