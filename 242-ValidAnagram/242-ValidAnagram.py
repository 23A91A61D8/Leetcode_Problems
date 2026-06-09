# Last updated: 09/06/2026, 15:51:31
1class Solution(object):
2    def isAnagram(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        if sorted(s) == sorted(t):
9            return True
10        else:
11            return False
12        