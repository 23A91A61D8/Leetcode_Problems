# Last updated: 01/09/2026, 18:39:59
1class Solution(object):
2    def missingMultiple(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        multiple = k
9        while multiple in nums:
10            multiple += k
11        return multiple
12
13        