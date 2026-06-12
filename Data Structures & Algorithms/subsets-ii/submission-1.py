class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtrack(start, cand):
            if start == len(nums):
                res.append(cand.copy())
                return
            
            # subsets that include nums[start]
            cand.append(nums[start])
            backtrack(start + 1, cand)
            cand.pop()
            
            # subsets that don't include nums[start] shouldn't include any duplicates 
            while start + 1 < len(nums) and nums[start] == nums[start+1]:
                start += 1
            
            backtrack(start + 1, cand)
        
        backtrack(0, [])

        return res

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
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