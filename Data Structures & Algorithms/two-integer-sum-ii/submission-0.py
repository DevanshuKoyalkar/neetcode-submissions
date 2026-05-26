class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        LEN = len(nums)

        start, end = 0, LEN - 1


        while start < end:
            curr_sum = nums[start] + nums[end]
            if curr_sum == target:
                return [start + 1, end + 1]
            elif curr_sum > target:
                end -= 1
            else:
                start += 1
        
        return []