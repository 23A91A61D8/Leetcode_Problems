# Last updated: 30/06/2026, 21:41:41
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        total = 0
        n = len(arr)
        for i in range(n):
            for j in range(i,n):
                subarray = arr[i:j+1]
                if len(subarray) % 2 == 1:
                    total += sum(subarray)
        return total


        