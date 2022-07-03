class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        maxProfit = 0
        profit = 0
        while end < len(prices):
            if prices[end] < prices[start]:
                start = end
                end = end + 1
            else:
                profit = prices[end] - prices[start]
                end = end + 1
            maxProfit = max(profit, maxProfit)
        return maxProfit   