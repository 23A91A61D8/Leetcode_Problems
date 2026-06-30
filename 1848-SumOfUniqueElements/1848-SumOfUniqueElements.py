# Last updated: 30/06/2026, 21:41:30
class Solution(object):
    def sumOfUnique(self, nums):
        freq = {}
        total = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            if freq[num] == 1:
                total += num
        return total
