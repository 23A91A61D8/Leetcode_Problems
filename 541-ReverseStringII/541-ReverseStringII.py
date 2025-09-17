# Last updated: 17/09/2025, 20:42:27
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)   
        for i in range(0, len(s), 2 * k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
