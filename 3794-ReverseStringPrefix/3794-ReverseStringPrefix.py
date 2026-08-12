# Last updated: 12/08/2026, 22:31:28
1class Solution(object):
2    def reversePrefix(self, s, k):
3        """
4        :type s: str
5        :type k: int
6        :rtype: str
7        """
8        return s[:k][::-1] +s[k:]
9
10
11        