# Last updated: 18/08/2026, 22:52:36
1class Solution(object):
2    def largestInteger(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        n = len(nums)
9        count = {}
10        for i in range(n-k+1):
11            sub = set(nums[i:i+k])
12            for x in sub:
13                count[x] = count.get(x,0) + 1
14        candidates = [x for x in count if count[x] == 1]
15        return max(candidates) if candidates else -1