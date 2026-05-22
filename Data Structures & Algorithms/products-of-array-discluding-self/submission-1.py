class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        # n = len(nums)
        # left_product = [1] * n
        # right_product = [1] * n

        # for i in range(1, n):
        #     left_product[i] = left_product[i-1] * nums[i-1]
        
        # for i in range(n-2, -1, -1):
        #     right_product[i] = right_product[i+1] * nums[i+1]
        
        # result = [1] * n

        # for i in range(n):
        #     result[i] = left_product[i] * right_product[i]
        
        # return result

        n = len(nums)
        result = [1] * n

        for i in range(1,n):
            result[i] = result[i-1] * nums[i-1]
        
        postfix = 1

        for i in range(n-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result











