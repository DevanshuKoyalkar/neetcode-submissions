class Solution:
    def canJump(self, nums: List[int]) -> bool:
       
        start, end = 0, nums[0]
        queue = deque([0])
        n = len(nums)

        while start <= end and start < n:
            end = max(end, nums[start] + start)
            start += 1

            # print(start, end)
        
        return end >= n - 1


    
        



        