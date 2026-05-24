class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # find where it was rotated in logn 
        # find where it is in the right section


        LEN = len(nums)

        # nums[mid] >= nums[0]
        # [3,4,5,6,1,2]
        #  T T T T F F
        
        # find first False
        #  T F F F F F
        #  0 1 2 3 4 5

        start, end = 0, LEN - 1

        pivot = LEN

        while start <= end:
            mid = (start + end) // 2

            print(start, end, mid, nums[mid], nums[0])

            if nums[mid] >= nums[0]:
                start = mid + 1
            else:
                pivot = mid
                end = mid - 1

        # print(nums, pivot, nums[pivot])

        if pivot < LEN and nums[pivot] <= target <= nums[LEN - 1]: # second half
            start, end = pivot, LEN - 1
        else: # first half
            start, end = 0, pivot - 1


        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        # not found
        return -1 

        



