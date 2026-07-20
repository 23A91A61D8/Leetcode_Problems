# Last updated: 20/07/2026, 21:32:13
1class Solution(object):
2    def shiftGrid(self, grid, k):
3        m, n = len(grid), len(grid[0])
4        total = m * n
5        flat = []
6        for row in grid:
7            flat.extend(row)
8        k = k % total
9        if k == 0:
10            return grid
11        flat = flat[-k:] + flat[:-k]
12        new_grid = []
13        for i in range(m):
14            new_grid.append(flat[i*n:(i+1)*n])
15        return new_grid
16