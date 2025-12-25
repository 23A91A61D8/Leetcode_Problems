# Last updated: 25/12/2025, 21:40:22
1class Solution(object):
2    def intersection(self, nums1, nums2):
3        """
4        :type nums1: List[int]
5        :type nums2: List[int]
6        :rtype: List[int]
7        """
8        set1 = set(nums1)
9        set2 = set(nums2)
10        result = set1 & set2
11        return list(result)