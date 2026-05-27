class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        LEN = len(gas)

        if sum(gas) - sum(cost) < 0:
            return -1
        
        result = 0
        total = 0
        for i in range(LEN):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                result = (i + 1) % LEN
        
        return result