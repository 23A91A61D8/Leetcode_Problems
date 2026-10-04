# Last updated: 04/10/2026, 14:00:09
1class Solution(object):
2    def checkValidString(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        low = 0
8        high = 0
9        for ch in s:
10            if ch == '(':
11                low += 1
12                high += 1
13            elif ch == ')':
14                low -= 1
15                high -= 1
16            else:  
17                low -= 1       
18                high += 1      
19            if high < 0:
20                return False
21            low = max(low, 0)
22        return low == 0
23