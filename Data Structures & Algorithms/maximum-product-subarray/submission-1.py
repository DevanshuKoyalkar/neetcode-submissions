class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        LEN = len(nums)
        max_product = [1] * LEN
        min_product = [1] * LEN

        max_product[0] = nums[0]
        min_product[0] = nums[0]

        result = max_product[0]

        for i in range(1, LEN):
            if nums[i] >= 0:
                max_product[i] = max(nums[i], max_product[i-1] * nums[i])
                min_product[i] = min(nums[i], min_product[i-1] * nums[i])
            else:
                max_product[i] = max(nums[i], min_product[i-1] * nums[i])
                min_product[i] = min(nums[i], max_product[i-1] * nums[i])

            result = max(max_product[i], result)

        print(max_product)
        print(min_product)
        
        return result