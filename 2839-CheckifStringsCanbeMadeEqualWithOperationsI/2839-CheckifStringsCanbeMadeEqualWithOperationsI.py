# Last updated: 21/08/2026, 21:58:57
1class Solution(object):
2    def canBeEqual(self, s1, s2):
3        return sorted([s1[0], s1[2]]) == sorted([s2[0], s2[2]]) and \
4               sorted([s1[1], s1[3]]) == sorted([s2[1], s2[3]])
5