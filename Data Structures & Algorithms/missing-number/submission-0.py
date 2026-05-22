class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)

        for i in range(n):
            result ^= i
            result ^= nums[i]
        
        result ^= n
        return result