class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        SUM = sum(nums)

        if SUM % 2 == 1: return False
        target = SUM // 2

        dp = set()
        dp.add(0)

        for num in nums:
            next_dp = set()

            for val in dp:
                next_dp.add(val)
                next_dp.add(val + num)
            
            
            dp = next_dp
            if target in dp:
                return True

        return target in dp

