# Last updated: 12/06/2026, 21:56:07
1class Solution(object):
2    def plusOne(self, digits):
3        n = len(digits)
4        for i in range(n - 1, -1, -1):
5            if digits[i] < 9:   
6                digits[i] += 1
7                return digits
8            else:               
9                digits[i] = 0
10        return [1] + digits
11