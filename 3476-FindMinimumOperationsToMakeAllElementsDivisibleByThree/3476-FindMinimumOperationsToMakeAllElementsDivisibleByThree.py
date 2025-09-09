# Last updated: 09/09/2025, 14:16:59
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if num % 3 != 0:
                count += 1
        return count