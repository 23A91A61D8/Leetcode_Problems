# Last updated: 23/09/2026, 21:43:36
1class Solution(object):
2    def minOperations(self, nums, x):
3        """
4        :type nums: List[int]
5        :type x: int
6        :rtype: int
7        """
8        total = sum(nums)
9        target = total - x
10        if target < 0:
11            return -1
12        left = 0
13        curr_sum = 0
14        max_len = -1
15        for right in range(len(nums)):
16            curr_sum += nums[right]
17            while left <= right and curr_sum > target:
18                curr_sum -= nums[left]
19                left += 1
20            if curr_sum == target:
21                max_len = max(max_len, right - left + 1)
22        return -1 if max_len == -1 else len(nums) - max_len