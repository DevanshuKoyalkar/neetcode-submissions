class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permute = []

        def backtrack(start):
            if start == len(nums):
                permute.append(nums[:])  # Append a copy of the current permutation
                return
            
            # swapping start with ith position
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return permute

    def permute2(self, nums: List[int]) -> List[List[int]]:
        LEN = len(nums)
        if LEN == 0:
            return []

        if LEN == 1:
            return [nums]
        
        result = []

        tail_permutes = self.permute(nums[1:])
        num = nums[0]

        for tail_permute in tail_permutes:
            for i in range(LEN):
                result.append(tail_permute[:i] + [num] + tail_permute[i:])
        
        return result



