class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        LEN = len(cost)

        # min cost to reach an index i
        before_last, last = 0, 0


        for i in range(2, LEN + 1):
            curr  = min(
                cost[i-1] + last, 
                cost[i-2] + before_last
            )
            before_last = last
            last = curr

        
        # print(min_cost_to_reach)
        return last

