# Last updated: 27/12/2025, 22:03:40
1class Solution(object):
2    def containsNearbyDuplicate(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: bool
7        """
8        last_index = {}
9
10        for i in range(len(nums)):
11            if nums[i] in last_index:
12                if i - last_index[nums[i]] <= k:
13                    return True
14            last_index[nums[i]] = i
15
16        return False