class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0


        # at every node state --> sold, didn't sel and prev didn't sell, dint' sell and prev old
        # sold --> 

        #dp[i] # max after you have sold at i
        # 0 is you sold at i 
        # 1 is you didn't sell at i
        # you need to know cost base from prev!
        # dp = [[0,0] for _ in len(prices)]



        # decision tree --> at each position buy, sell or do nothing
        # state is total profit till now + when have I last sold + if I bought something + price

        buy, sell, cooldown = -prices[0], 0, 0


        for i in range(1, len(prices)):
            new_buy = max(buy, cooldown - prices[i])

            new_sell = max(sell, buy + prices[i])

            new_cooldown = sell

            buy, sell, cooldown = new_buy, new_sell, new_cooldown

        return max(sell, cooldown) # 
