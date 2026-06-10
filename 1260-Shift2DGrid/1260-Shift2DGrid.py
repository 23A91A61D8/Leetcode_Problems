# Last updated: 10/06/2026, 12:59:28
1class Solution(object):
2    def shiftGrid(self, grid, k):
3
4        m = len(grid)
5        n = len(grid[0])
6
7        nums = []
8
9        for row in grid:
10            nums.extend(row)
11
12        k = k % (m * n)
13
14        nums = nums[-k:] + nums[:-k]
15
16        result = []
17
18        for i in range(0, len(nums), n):
19            result.append(nums[i:i+n])
20
21        return result