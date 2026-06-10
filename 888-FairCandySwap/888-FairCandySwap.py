# Last updated: 10/06/2026, 12:25:54
1class Solution(object):
2    def fairCandySwap(self, aliceSizes, bobSizes):
3
4        aliceSum = sum(aliceSizes)
5        bobSum = sum(bobSizes)
6
7        diff = (bobSum - aliceSum) // 2
8
9        bobSet = set(bobSizes)
10
11        for a in aliceSizes:
12
13            if a + diff in bobSet:
14                return [a, a + diff]