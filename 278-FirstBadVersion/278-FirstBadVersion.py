# Last updated: 12/08/2026, 22:30:30
1# The isBadVersion API is already defined for you.
2# @param version, an integer
3# @return a bool
4# def isBadVersion(version):
5
6class Solution(object):
7    def firstBadVersion(self, n):
8        """
9        :type n: int
10        :rtype: int
11        """
12        low , high = 1, n
13        while low < high:
14            mid = (low + high) //2
15            if isBadVersion(mid):
16                high = mid
17            else:
18                low = mid + 1
19        return low
20        