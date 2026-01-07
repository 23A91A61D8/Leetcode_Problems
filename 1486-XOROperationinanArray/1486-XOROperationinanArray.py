# Last updated: 07/01/2026, 22:40:21
1class Solution(object):
2    def xorOperation(self, n, start):
3        """
4        :type n: int
5        :type start: int
6        :rtype: int
7        """
8        ans = 0
9        for i in range(n):
10            ans  ^= start + 2 * i
11        return ans
12
13