class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        # naive is n^3
        # given i --> find j and k in O(n)
        result = []
        n = len(nums)
        if n < 3: return []

        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = n - 1

            target = -1 * nums[i]

            while start < end:
                pair_sum = nums[start] + nums[end]

                if pair_sum == target:
                    result.append([nums[i], nums[start], nums[end]])

                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    
                    start += 1
                    end -= 1

                elif pair_sum > target:
                    end -= 1
                elif pair_sum < target:
                    start += 1
        return result
