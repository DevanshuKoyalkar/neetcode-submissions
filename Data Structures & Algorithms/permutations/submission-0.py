class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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



