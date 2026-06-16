# Last updated: 16/06/2026, 22:20:13
1class Solution(object):
2    def countOdds(self, low, high):
3        """
4        :type low: int
5        :type high: int
6        :rtype: int
7        """
8        return ((high - low) // 2) + (1 if (low % 2 == 1 or high % 2 == 1) else 0)
9