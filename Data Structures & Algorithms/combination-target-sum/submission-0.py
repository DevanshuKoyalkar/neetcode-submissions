class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start, curr, total):
            if total == target:
                result.append(curr.copy())
                return

            if start >= len(nums) or total > target:
                return
            
            # include
            curr.append(nums[start])
            dfs(start, curr, total + nums[start])
            curr.pop()

            # exclude
            dfs(start + 1, curr, total)
        
        dfs(0, [], 0)
        return result
        

        
        