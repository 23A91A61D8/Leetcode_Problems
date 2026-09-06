# Last updated: 06/09/2026, 18:39:26
1class Solution(object):
2    def countSymmetricIntegers(self, low, high):
3        count = 0
4        for num in range(low, high + 1):
5            s = str(num)
6            n = len(s)
7            if n % 2 == 0:
8                mid = n // 2
9                if sum(map(int, s[:mid])) == sum(map(int, s[mid:])):
10                    count += 1
11        return count
12        
13