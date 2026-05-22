class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = s.lower()


        left, right = 0, len(s) - 1

        while left < right:

            while left < right and not clean_s[right].isalnum():
                right -= 1
            
            while left < right and not clean_s[left].isalnum():
                left += 1
            
            if clean_s[left] != clean_s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True


