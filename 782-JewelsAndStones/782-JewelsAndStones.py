# Last updated: 30/06/2026, 21:42:38
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        for s in stones:
            if s in jewels:
                count += 1
        return count