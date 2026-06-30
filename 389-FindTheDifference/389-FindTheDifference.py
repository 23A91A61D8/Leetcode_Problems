# Last updated: 30/06/2026, 21:43:20
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for ch in t:
            if t.count(ch) != s.count(ch):
                return ch

        