# Last updated: 10/06/2026, 12:32:02
1class Solution(object):
2    def findJudge(self, n, trust):
3        count = [0] * (n + 1)
4        for a, b in trust:
5            count[a] -= 1
6            count[b] += 1
7        for i in range(1, n + 1):
8            if count[i] == n - 1:
9                return i
10        return -1