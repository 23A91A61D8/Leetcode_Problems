# Last updated: 13/08/2026, 22:12:24
1class Solution(object):
2    def isToeplitzMatrix(self, matrix):
3        """
4        :type matrix: List[List[int]]
5        :rtype: bool
6        """
7        m = len(matrix)
8        n = len(matrix[0])
9        for i in range(1,m):
10            for j in range(1,n):
11                if matrix[i][j] != matrix[i-1][j-1]:
12                    return False
13        return True        