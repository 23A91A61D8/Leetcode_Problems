# Last updated: 12/06/2026, 21:50:57
1class Solution(object):
2    def repeatedSubstringPattern(self, s):
3        return s in (s + s)[1:-1]
4        