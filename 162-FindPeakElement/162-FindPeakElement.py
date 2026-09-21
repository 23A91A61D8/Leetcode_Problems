# Last updated: 21/09/2026, 21:11:23
1class Solution(object):
2    def findPeakElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        left = 0 
8        right = len(nums) - 1
9        while left < right:
10            mid = (left + right) // 2
11            if nums[mid] < nums[mid + 1]:
12                left = mid + 1
13            else:
14                right = mid 
15        return left 
16        