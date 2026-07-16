# Last updated: 16/07/2026, 22:37:40
1from fractions import gcd
2
3class Solution(object):
4    def gcdSum(self, nums):
5        n = len(nums)
6        prefixGcd = []
7        mxi = nums[0]
8        for i in range(n):
9            mxi = max(mxi, nums[i])
10            prefixGcd.append(gcd(nums[i], mxi))
11        prefixGcd.sort()
12        total = 0
13        left, right = 0, n - 1
14        while left < right:
15            total += gcd(prefixGcd[left], prefixGcd[right])
16            left += 1
17            right -= 1
18        return total
19