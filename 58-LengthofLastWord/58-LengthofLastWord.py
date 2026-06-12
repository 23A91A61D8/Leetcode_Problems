# Last updated: 12/06/2026, 21:45:28
1class Solution(object):
2    def lengthOfLastWord(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        return len(s.strip().split()[-1])
8
9        