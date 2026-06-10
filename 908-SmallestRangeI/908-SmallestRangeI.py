# Last updated: 10/06/2026, 12:28:49
1class Solution(object):
2    def smallestRangeI(self, nums, k):
3        maximum = max(nums)
4        minimum = min(nums)
5        score = maximum - minimum
6        return max(0, score - 2 * k)
7        