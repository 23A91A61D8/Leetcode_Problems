# Last updated: 06/01/2026, 22:05:16
1class Solution(object):
2    def numWaterBottles(self, numBottles, numExchange):
3        total = numBottles
4        empty = numBottles
5
6        while empty >= numExchange:
7            new_bottles = empty // numExchange
8            total += new_bottles
9            empty = new_bottles + (empty % numExchange)
10
11        return total
12