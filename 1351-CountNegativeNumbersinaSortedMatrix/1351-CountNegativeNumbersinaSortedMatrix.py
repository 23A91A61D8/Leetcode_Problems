# Last updated: 28/12/2025, 22:20:01
1class Solution(object):
2    def countNegatives(self, grid):
3        count = 0
4
5        for row in grid:
6            for num in row:
7                if num < 0:
8                    count += 1
9        return count
10