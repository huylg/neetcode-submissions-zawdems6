class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        result = 0

        for i, price in enumerate(prices):
            if price < prices[buy]:
                buy = i
            else:
                result = max(price - prices[buy], result)

        return result
