# Last updated: 10/06/2026, 13:04:44
1class Solution(object):
2    def truncateSentence(self, s, k):
3        words = s.split()
4        return " ".join(words[:k])