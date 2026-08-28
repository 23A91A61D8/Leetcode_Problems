# Last updated: 28/08/2026, 21:25:14
1class Solution(object):
2    def judgeCircle(self, moves):
3        return moves.count('U') == moves.count('D') and \
4               moves.count('L') == moves.count('R')