# Last updated: 03/07/2026, 22:03:15
1class Solution(object):
2    def reverseWords(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        return " ".join(word[::-1]for word in s.split())
8        