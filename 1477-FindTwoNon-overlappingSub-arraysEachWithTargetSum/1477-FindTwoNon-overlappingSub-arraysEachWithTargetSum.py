# Last updated: 17/09/2026, 23:02:56
1class Solution(object):
2    def minSumOfLengths(self, arr, target):
3        n = len(arr)
4        INF = n + 1
5        best = [INF] * (n + 1)
6        left = 0
7        curr_sum = 0
8        ans = INF
9        for right in range(n):
10            curr_sum += arr[right]
11            while curr_sum > target:
12                curr_sum -= arr[left]
13                left += 1
14            if curr_sum == target:
15                length = right - left + 1
16                if best[left] != INF:
17                    ans = min(ans, length + best[left])
18                best[right + 1] = min(best[right], length)
19            else:
20                best[right + 1] = best[right]
21        return -1 if ans == INF else ans
22