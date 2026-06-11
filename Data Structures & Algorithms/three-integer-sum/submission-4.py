class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i, a in enumerate(nums):
            if a > 0:   # b, c are also positive 
                break
            
            if i > 0 and a == nums[i - 1]:
                continue

            
            l, r = i + 1, len(nums) - 1

            while l < r:
                b, c = nums[l], nums[r]
                threeSum = a + b + c


                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,b,c])
                    l += 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res
