# Last updated: 30/06/2026, 21:43:21
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1
        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        return result
        

