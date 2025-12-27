# Last updated: 27/12/2025, 21:12:19
1class Solution(object):
2    def intersect(self, nums1, nums2):
3        """
4        :type nums1: List[int]
5        :type nums2: List[int]
6        :rtype: List[int]
7        """
8        result = []
9        freq = {}
10        for num in nums1:
11            freq[num] = freq.get(num, 0) + 1
12        for num in nums2:
13            if num in freq and freq[num] > 0:
14                result.append(num)
15                freq[num] -= 1
16        return result
17        
18
19