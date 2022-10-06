class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''Brute Force'''
        # maximum = 0
        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         if prices[j] - prices[i] > maximum:
        #             maximum = prices[j] - prices[i]
        # return maximum
        
        '''O(n)'''
        profit, max_profit = 0, 0
        start, end = 0, 1
        while end < len(prices):
            if prices[end] < prices[start]:
                start = end
                end += 1
                continue
            profit = prices[end] - prices[start]
            if max_profit < profit:
                max_profit = profit
            end += 1
        return max_profit