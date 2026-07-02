# Last updated: 02/07/2026, 23:42:04
1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        seen = {}
9        for index, num in enumerate(nums):
10            complement = target - num
11            if complement in seen:
12                return [seen[complement], index]
13            seen[num] = index
14            
15