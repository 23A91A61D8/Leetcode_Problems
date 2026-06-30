# Last updated: 30/06/2026, 21:43:11
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 0
        while n >= row + 1:  
            row += 1
            n -= row
        return row
