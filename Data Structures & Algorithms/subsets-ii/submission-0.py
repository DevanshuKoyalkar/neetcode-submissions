class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        LEN = len(nums)

        if not LEN:
            return [[]]
        
        nums.sort()

        first = nums[0]
        result = []

        # say first is 2
        # contains 2 case
        tail_subsets = self.subsetsWithDup(nums[1:])

        for tail_subset in tail_subsets:
            result.append(tail_subset + [first])
        
        # doesn't contain 2 --> skip all 2's
        next_idx = 1
        while next_idx < LEN and nums[next_idx] == first:
            next_idx += 1
        
        no_first_element_subsets = self.subsetsWithDup(nums[next_idx:])

        result += no_first_element_subsets

        return result
        


