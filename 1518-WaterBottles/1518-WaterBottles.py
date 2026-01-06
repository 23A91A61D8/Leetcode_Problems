# Last updated: 06/01/2026, 22:05:36
1class Solution(object):
2    def numWaterBottles(self, numBottles, numExchange):
3        total = numBottles
4        empty = numBottles
5        while empty >= numExchange:
6            new_bottles = empty // numExchange
7            total += new_bottles
8            empty = new_bottles + (empty % numExchange)
9
10        return total
11