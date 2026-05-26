class Solution:
    digit_to_letter = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
    
    def letterCombinations(self, digits: str) -> List[str]:
        LEN = len(digits)
        result = []

        if LEN == 0: 
            return result
        
        if LEN == 1:
            return [ch for ch in self.digit_to_letter[digits]]
            
        tail_result = self.letterCombinations(digits[1:]) 
        
        for cand in tail_result:
            print(digits[0], self.digit_to_letter[digits[0]])
            for char in self.digit_to_letter[digits[0]]:
                
                result.append(char + cand)
        
        return result

