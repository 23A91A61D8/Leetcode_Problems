# Last updated: 10/06/2026, 12:56:34
1class Solution(object):
2    def heightChecker(self, heights):
3
4        expected = sorted(heights)
5
6        count = 0
7
8        for i in range(len(heights)):
9
10            if heights[i] != expected[i]:
11                count += 1
12
13        return count