# Last updated: 30/06/2026, 21:41:34
class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max(sum(customers) for customers in accounts)
        