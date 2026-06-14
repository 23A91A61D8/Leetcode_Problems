# Last updated: 14/06/2026, 22:10:12
1class Solution(object):
2    def maximumWealth(self, accounts):
3        """
4        :type accounts: List[List[int]]
5        :rtype: int
6        """
7        return max(sum(customers) for customers in accounts)
8        