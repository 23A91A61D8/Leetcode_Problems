# Last updated: 23/06/2026, 22:34:06
1class Solution(object):
2    def isPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        cleaned =  ''.join(ch.lower() for ch in s if ch.isalnum())
8        return cleaned == cleaned[::-1]
9