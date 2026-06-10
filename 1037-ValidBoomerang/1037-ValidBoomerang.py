# Last updated: 10/06/2026, 12:33:07
1class Solution(object):
2    def isBoomerang(self, points):
3        x1, y1 = points[0]
4        x2, y2 = points[1]
5        x3, y3 = points[2]
6        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)