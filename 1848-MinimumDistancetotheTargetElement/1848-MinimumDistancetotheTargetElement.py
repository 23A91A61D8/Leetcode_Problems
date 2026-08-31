# Last updated: 31/08/2026, 21:47:05
1class Solution(object):
2    def getMinDistance(self, nums, target, start):
3        """
4        :type nums: List[int]
5        :type target: int
6        :type start: int
7        :rtype: int
8        """
9        ans = float('inf')
10        for i in range(len(nums)):
11            if nums[i] == target:
12                ans = min(ans, abs(i - start))
13        return ans
14