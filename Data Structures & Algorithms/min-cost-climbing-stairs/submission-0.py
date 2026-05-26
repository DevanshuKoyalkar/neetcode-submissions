class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        LEN = len(cost)

        # min cost to reach an index i
        min_cost_to_reach = [0] * (LEN + 1)

        for i in range(2, LEN + 1):
            min_cost_to_reach[i] = min(
                cost[i-1] + min_cost_to_reach[i-1], 
                cost[i-2] + min_cost_to_reach[i-2]
            )
        
        # print(min_cost_to_reach)
        return min_cost_to_reach[LEN]

