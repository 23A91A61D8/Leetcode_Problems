# Last updated: 28/06/2026, 20:40:39
1class Solution(object):
2    def lengthOfLastWord(self, s):
3        return len(s.strip().split()[-1])
4