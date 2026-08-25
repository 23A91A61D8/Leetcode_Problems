# Last updated: 25/08/2026, 22:16:18
1class Solution(object):
2    def isThree(self, n):
3        """
4        :type n: int
5        :rtype: bool
6        """
7        count = 0
8        for i in range(1, n+1):
9            if n % i == 0:
10                count += 1
11        return count == 3
12
13        