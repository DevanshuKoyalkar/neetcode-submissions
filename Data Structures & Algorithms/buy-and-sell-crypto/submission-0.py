class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            # print(price, min_price, max_profit)
            min_price = min(min_price, price)
        return max_profit