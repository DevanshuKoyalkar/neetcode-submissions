class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        result = nums[0]
        counter = 1

        for i in range(1, len(nums)):
            num = nums[i]
            if num == result:
                counter += 1
            else:
                if counter == 0:
                    result = num
                    counter = 1
                else:
                    counter -= 1
            
        
        return result

