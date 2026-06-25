# Last updated: 25/06/2026, 15:52:27
1class Solution(object):
2    def addBinary(self, a, b):
3        """
4        :type a: str
5        :type b: str
6        :rtype: str
7        """
8        a = int(a,2)
9        b = int(b,2)
10        result = a+b
11        return bin(result)[2:]