class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i, j = 0, 1

        maxProfit = 0

        while j < len(prices):
            if prices[i] < prices[j]:
                maxProfit = max(maxProfit, prices[j] - prices[i])
            else:
                i = j
            
            j += 1

        return maxProfit

        # left, right = 0, 1
        # profit = 0

        # while right < len(prices):
        #     if prices[left] < prices[right]:
        #         profit = max(profit, prices[right] - prices[left])
        #     else:
        #         left = right
        #     right += 1
        # return profit
        