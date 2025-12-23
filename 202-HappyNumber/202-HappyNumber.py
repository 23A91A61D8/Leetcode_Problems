# Last updated: 23/12/2025, 23:16:26
1class Solution(object):
2    def isHappy(self, n):
3        seen = set()
4        while n != 1:
5            if n in seen:
6                return False
7            seen.add(n)
8            total = 0
9            while n > 0:
10                digit = n % 10
11                total += digit * digit
12                n //= 10
13
14            n = total
15        return True
16