# Last updated: 01/01/2026, 21:38:03
1class Solution(object):
2    def fib(self, n):
3        if n == 0:
4            return 0
5        if n == 1:
6            return 1
7        a, b = 0, 1
8        for i in range(2, n + 1):
9            a, b = b, a + b
10        return b
11