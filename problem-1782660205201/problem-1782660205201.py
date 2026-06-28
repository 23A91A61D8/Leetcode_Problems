# Last updated: 28/06/2026, 20:53:25
1class Solution(object):
2    def lengthOfLastWord(self, s):
3        return len(s.strip().split()[-1])
4