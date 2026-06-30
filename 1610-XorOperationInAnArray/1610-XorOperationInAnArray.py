# Last updated: 30/06/2026, 21:41:50
class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        ans = 0
        for i in range(n):
            ans  ^= start + 2 * i
        return ans

