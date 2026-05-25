class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        LEN = len(nums)

        num_sum = sum(nums)

        if num_sum % 2 == 1: 
            return False
        
        target = num_sum // 2

        nums.sort()
        # select or dont' select 

        def dfs(pos, current_sum):
            if current_sum == target:
                return True
            
            if pos >= LEN or current_sum > target:
                return False
            
            # select element
            return dfs(pos + 1, current_sum + nums[pos]) or dfs(pos + 1, current_sum)
            

        return dfs(0, 0)

