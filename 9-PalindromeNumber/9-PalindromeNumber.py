# Last updated: 09/09/2025, 22:45:37
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        return str(x) == str(x)[::-1]
