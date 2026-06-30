# Last updated: 30/06/2026, 21:44:27
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.strip().split()[-1])
