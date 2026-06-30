# Last updated: 30/06/2026, 21:45:18
1class Solution(object):
2    def reverseWords(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7
8        return " ".join(s.strip().split()[::-1])
9        