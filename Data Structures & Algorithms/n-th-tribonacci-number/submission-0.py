class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1

        if n < 2: return n
        if n == 2: return 1

        for i in range(3, n + 1):
            # print(a,b,c)
            res = a + b + c
            if i % 3 == 0:
                a = res
            elif i % 3 == 1:
                b = res
            else:
                c = res
            
            # print(i, res)
            if i == n:
                return res
        
        return 0
            

            