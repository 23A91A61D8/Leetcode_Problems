# Last updated: 13/06/2026, 22:34:53
1class Solution(object):
2    def arraySign(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        for num in nums:
8            if num == 0:
9                return 0
10        negative_count = 0
11        for num in nums:
12            if num < 0:
13                negative_count += 1
14        return 1 if negative_count % 2 == 0 else -1
15