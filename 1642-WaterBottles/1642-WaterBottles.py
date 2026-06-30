# Last updated: 30/06/2026, 21:41:45
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = numBottles
        empty = numBottles
        while empty >= numExchange:
            new_bottles = empty // numExchange
            total += new_bottles
            empty = new_bottles + (empty % numExchange)

        return total
