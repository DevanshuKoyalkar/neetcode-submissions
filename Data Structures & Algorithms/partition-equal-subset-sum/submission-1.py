class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        LEN = len(nums)

        num_sum = sum(nums)

        if num_sum % 2 == 1: 
            return False
        
        target = num_sum // 2

        nums.sort()
        # select or dont' select 

        memo = {}

        def dfs(pos, current_sum):
            if (pos, current_sum) in memo:
                return memo[(pos, current_sum)]

            if current_sum == target:
                memo[(pos,current_sum)] = True
            
            elif pos >= LEN or current_sum > target:
                memo[(pos,current_sum)] = False
            
            else:
                # select element
                memo[(pos,current_sum)] = dfs(pos + 1, current_sum + nums[pos]) or dfs(pos + 1, current_sum)
            
            return memo[(pos,current_sum)]

        return dfs(0, 0)

