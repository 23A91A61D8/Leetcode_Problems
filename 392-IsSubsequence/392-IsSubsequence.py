# Last updated: 29/10/2026, 21:16:55
1
2class Solution(object):
3    def isSubsequence(self, s, t):
4        word = ""
5        for ch in t:
6            if ch in s[len(word):]:
7                if ch == s[len(word)]:
8                    word += ch
9            if len(word) == len(s):
10                return True
11        return len(word) == len(s)
12