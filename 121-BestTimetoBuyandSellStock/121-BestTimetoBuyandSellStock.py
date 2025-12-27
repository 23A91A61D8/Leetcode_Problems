# Last updated: 27/12/2025, 21:24:29
1class Solution(object):
2    def maxProfit(self, prices):
3        """
4        :type prices: List[int]
5        :rtype: int
6        """
7        min_price = float('inf')
8        max_profit = 0
9        for price in prices:
10            if price <min_price:
11                min_price = price
12            else:
13                profit = price - min_price
14                if profit > max_profit:
15                    max_profit = profit
16        return max_profit