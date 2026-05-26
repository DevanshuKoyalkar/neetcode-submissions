import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        MAX = max(piles)
        MIN = 1


        # F F F F T T 
        # invariant --> number of hours taken to eat is > H
        # first T such that we can each 

        start, end = MIN, MAX
        result = -1

        while start <= end:
            mid = (start + end) // 2

            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(float(pile) / mid)

            if num_hours > h:
                start = mid + 1
            else:
                result = mid
                end = mid - 1
        
        return result