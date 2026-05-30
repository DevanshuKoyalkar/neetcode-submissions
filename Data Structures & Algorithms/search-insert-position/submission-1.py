class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # T T T F F F

        # in variant is num < target and we need to find the first F

        start, end = 0, len(nums) - 1
        result = -1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                result = mid
                end = mid - 1

        if result == -1: result = len(nums)
        return result