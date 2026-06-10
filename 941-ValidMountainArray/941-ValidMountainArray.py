# Last updated: 10/06/2026, 12:30:26
1class Solution(object):
2    def validMountainArray(self, arr):
3        n = len(arr)
4        if n < 3:
5            return False
6        i = 0
7        while i + 1 < n and arr[i] < arr[i + 1]:
8            i += 1
9        if i == 0 or i == n - 1:
10            return False
11        while i + 1 < n and arr[i] > arr[i + 1]:
12            i += 1
13        return i == n - 1