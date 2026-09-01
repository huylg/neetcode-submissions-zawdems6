class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = ma = prices[0]

        result = 0

        for price in prices:
            if price > ma:
                ma = price
            elif price < mi:
                mi = ma = price
            result = max(ma - mi, result)

        return result
        
