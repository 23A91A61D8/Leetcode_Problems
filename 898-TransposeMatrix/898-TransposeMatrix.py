# Last updated: 30/06/2026, 21:42:35
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return [list(row) for row in zip(*matrix)]
        