# Last updated: 09/12/2025, 23:15:09
1class Solution(object):
2    def climbStairs(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        if n == 1:
8            return 1
9        
10        dp = [0] * (n + 1)
11        dp[1] = 1
12        dp[2] = 2
13        
14        for i in range(3, n + 1):
15            dp[i] = dp[i - 1] + dp[i - 2]
16        
17        return dp[n]
18