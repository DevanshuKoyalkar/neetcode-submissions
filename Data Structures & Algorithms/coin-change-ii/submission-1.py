class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        LEN = len(coins)

        coins.sort()
        
        # number of ways to get to number
        ways_to_target = [1] + [0] * amount 

        for coin in coins:
            for target in range(amount + 1):
                if target - coin >= 0:
                    ways_to_target[target] += ways_to_target[target - coin]
        
        # print(ways_to_target)
        return ways_to_target[amount]