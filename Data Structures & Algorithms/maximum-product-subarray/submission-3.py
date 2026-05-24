class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        LEN = len(nums)

        max_product = nums[0]
        min_product = nums[0]

        result = max_product

        for i in range(1, LEN):
            maxp, minp = max_product, min_product
            if nums[i] >= 0:
                max_product = max(nums[i], maxp * nums[i])
                min_product = min(nums[i], minp * nums[i])
            else:
                max_product = max(nums[i], minp * nums[i])
                min_product = min(nums[i], maxp * nums[i])

            result = max(max_product, result)
        
        return result