class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        def next_num(num):
            result = 0
            while num:
                digit = num % 10
                result += digit ** 2
                num = num // 10
            
            return result
        
        curr = n
        
        while curr:
            if curr in seen:
                return False
            
            if curr == 1:
                return True

            seen.add(curr)
            next = next_num(curr)
            curr = next
        
        return True
