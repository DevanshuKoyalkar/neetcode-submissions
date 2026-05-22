class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            if n & 1:
                count += 1
            n >>= 1
        
        return count

    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(0, n + 1):
            result.append(self.hammingWeight(i))
        
        return result
