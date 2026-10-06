# Last updated: 06/10/2026, 22:18:20
1class Solution(object):
2    def minAddToMakeValid(self, s):
3        open = 0
4        add = 0
5        for ch in s:
6            if ch == '(':
7                open += 1
8            else:
9                if open > 0:
10                    open -= 1
11                else:
12                    add += 1
13        return add + open
14