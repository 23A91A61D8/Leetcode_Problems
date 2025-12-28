# Last updated: 28/12/2025, 22:05:57
1class Solution(object):
2    def sumOfUnique(self, nums):
3        freq = {}
4        total = 0
5        for num in nums:
6            freq[num] = freq.get(num, 0) + 1
7        for num in freq:
8            if freq[num] == 1:
9                total += num
10        return total
11