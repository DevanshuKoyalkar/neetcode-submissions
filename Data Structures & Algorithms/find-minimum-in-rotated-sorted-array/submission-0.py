class Solution:
    def findMin(self, nums: List[int]) -> int:
        LEN = len(nums)

        # TTTTFFFF
        # FFFFTTTT

        # Find the invariant first
        # [3,4,5,6,1,2]
        #  T T T T F F


        # nums[mid] >= nums[0]
        # find the first FALSE

        start, end = 0, LEN - 1
        result = 0

        while start <= end:
            mid = (start + end) // 2
            print(start, end, mid, nums[mid], nums[0])

            if nums[mid] >= nums[0]:
                start = mid + 1
            else:
                result = mid
                end = mid - 1

        return nums[result]

