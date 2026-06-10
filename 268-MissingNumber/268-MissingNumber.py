# Last updated: 10/06/2026, 12:15:58
1class Solution(object):
2    def missingNumber(self, nums):
3        n = len(nums)
4        for i in range(n + 1):
5            if i not in nums:
6                return i