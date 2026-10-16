# Last updated: 16/10/2026, 20:48:44
1class Solution(object):
2    def arrayPairSum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        nums.sort()
8        total = 0 
9        for i in range(0, len(nums), 2):
10            total += nums[i]
11        return total
12
13
14        