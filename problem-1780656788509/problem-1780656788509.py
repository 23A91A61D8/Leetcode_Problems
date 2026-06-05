# Last updated: 05/06/2026, 16:23:08
1class Solution(object):
2    def findTheDifference(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: str
7        """
8        for ch in t:
9            if t.count(ch) != s.count(ch):
10                return ch
11
12        