# Last updated: 30/08/2026, 21:52:20
1class Solution(object):
2    def findMiddleIndex(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        total = sum(nums)
8        left_sum = 0
9        for i in range(len(nums)):
10            right_sum = total - left_sum - nums[i]
11            if left_sum == right_sum:
12                return i
13            left_sum += nums[i]
14        return -1