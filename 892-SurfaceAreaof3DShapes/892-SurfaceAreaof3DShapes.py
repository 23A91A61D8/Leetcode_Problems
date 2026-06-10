# Last updated: 10/06/2026, 12:27:25
1class Solution(object):
2    def surfaceArea(self, grid):
3        n = len(grid)
4        area = 0
5        for i in range(n):
6            for j in range(n):
7                if grid[i][j] > 0:
8                    area += 2
9                    area += 4 * grid[i][j]
10                    if i > 0:
11                        area -= 2 * min(grid[i][j], grid[i-1][j])
12                    if j > 0:
13                        area -= 2 * min(grid[i][j], grid[i][j-1])
14        return area