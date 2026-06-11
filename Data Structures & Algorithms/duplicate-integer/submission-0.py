from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = Counter(nums)

        for _, val in num_count.items():
            if val > 1:
                return True
        
        return False