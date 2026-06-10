# Last updated: 10/06/2026, 12:58:16
1class Solution(object):
2    def relativeSortArray(self, arr1, arr2):
3
4        result = []
5
6        for num in arr2:
7
8            while num in arr1:
9                result.append(num)
10                arr1.remove(num)
11
12        arr1.sort()
13
14        return result + arr1