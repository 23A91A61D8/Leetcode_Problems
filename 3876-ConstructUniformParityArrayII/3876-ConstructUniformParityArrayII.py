# Last updated: 05/09/2026, 16:37:53
1class Solution(object):
2    def uniformArray(self, nums1):
3        """
4        :type nums1: List[int]
5        :rtype: bool
6        """
7        min_odd = float('inf')
8        min_even = float('inf')
9        for x in nums1:
10            if x % 2 == 0:
11                min_even = min(min_even, x)
12            else:
13                min_odd = min(min_odd, x)
14        if min_odd == float('inf'):
15            return True
16        return min_odd < min_even
17