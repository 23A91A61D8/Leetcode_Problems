# Last updated: 26/12/2025, 23:03:29
1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        for num in set(nums):
8            if nums.count(num) > len(nums)//2:
9                return num