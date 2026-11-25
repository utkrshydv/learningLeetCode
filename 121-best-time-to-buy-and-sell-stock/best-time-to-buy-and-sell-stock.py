class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest_price = 9999999
        highest_profit = -9999999

        for price in prices:
            lowest_price = min(lowest_price, price)
            highest_profit = max(highest_profit, price - lowest_price)

        return highest_profit

        