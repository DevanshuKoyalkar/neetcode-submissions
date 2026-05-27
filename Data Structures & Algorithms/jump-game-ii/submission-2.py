class Solution:
    def jump(self, nums: List[int]) -> int:
        # bfs 

        LEN = len(nums)
        if LEN == 1: return 0

        start, end = 1, nums[0]

        num_jumps = 1
        while end < LEN:
            if end == LEN - 1:
                break
            num_jumps += 1
            max_reachable = 0
            while start <= end:
                max_reachable = max(max_reachable, start + nums[start])
                start += 1
            end = max_reachable
            
            
        return num_jumps
        