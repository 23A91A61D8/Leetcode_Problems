# Last updated: 10/06/2026, 12:23:44
1class Solution(object):
2    def majorityElement(self, nums):
3        count = 0
4        candidate = None
5        for num in nums:
6            if count == 0:
7                candidate = num
8            if num == candidate:
9                count += 1
10            else:
11                count -= 1
12        return candidate