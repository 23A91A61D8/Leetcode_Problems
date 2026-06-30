# Last updated: 30/06/2026, 21:41:48
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return ((high - low) // 2) + (1 if (low % 2 == 1 or high % 2 == 1) else 0)
