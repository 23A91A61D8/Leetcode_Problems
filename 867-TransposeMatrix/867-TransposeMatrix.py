# Last updated: 24/09/2025, 18:58:20
class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return [list(row) for row in zip(*matrix)]
        