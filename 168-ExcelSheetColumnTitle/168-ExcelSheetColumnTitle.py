# Last updated: 09/09/2025, 14:19:52
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1  
            ans = chr(columnNumber % 26 + ord("A")) + ans
            columnNumber //= 26
        return ans
