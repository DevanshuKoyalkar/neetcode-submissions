import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sum_piles = sum(piles)

        MAX = 1_000_000_000
        MIN = 1


        # F F F F T T 
        # invariant --> number of hours taken to eat is > H
        # first T such that we can each 

        start, end = MIN, MAX
        result = -1

        def get_hours(speed):
            res = 0
            for pile in piles:
                res += math.ceil(pile/speed)
            return res

        while start <= end:
            mid = (start + end) // 2

            num_hours = get_hours(mid)
            # print(start, end, mid, num_hours, h)

            if num_hours > h:
                start = mid + 1
            else:
                result = mid
                end = mid - 1
        
        return result