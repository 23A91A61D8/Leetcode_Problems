# Last updated: 10/06/2026, 13:11:56
1class Solution(object):
2    def isPalindrome(self, s):
3        new = ""
4        for ch in s:
5            if ch.isalnum():
6                new += ch.lower()
7        return new == new[::-1]