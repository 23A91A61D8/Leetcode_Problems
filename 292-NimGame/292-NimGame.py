# Last updated: 31/12/2025, 22:40:11
1class Solution(object):
2    def canWinNim(self, n):
3        """
4        :type n: int
5        :rtype: bool
6        """
7        if n % 4 != 0:
8            return True
9        else:
10            return False