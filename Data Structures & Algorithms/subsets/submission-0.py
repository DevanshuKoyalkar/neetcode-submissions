class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        LEN = len(nums)

        result = []

        if not LEN:
            return [[]]
        
        first = nums[0]

        # contains first
        tail_subsets = self.subsets(nums[1:])

        for tail_subset in tail_subsets:
            result.append(tail_subset + [first])
        
        # doesn't contain first
        no_first_subsets = tail_subsets

        result += tail_subsets


        return result