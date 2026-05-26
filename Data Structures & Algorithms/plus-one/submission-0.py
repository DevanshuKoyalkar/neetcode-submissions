class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, sum = 1, 0

        LEN = len(digits)

        for i in range(LEN - 1, -1, -1):
            carry, sum = divmod(carry + digits[i], 10)

            digits[i] = sum
        
        if carry != 0:
            digits = [1] + digits

        return digits
