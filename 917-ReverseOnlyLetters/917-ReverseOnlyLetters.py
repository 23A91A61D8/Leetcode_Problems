# Last updated: 18/12/2025, 22:59:09
1class Solution(object):
2    def reverseOnlyLetters(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        s = list(s)
8        left , right = 0, len(s) - 1
9        while left < right :
10            if not s[left].isalpha():
11                left += 1
12            elif not s[right].isalpha():
13                right -= 1
14            else:
15                s[left], s[right]  = s[right], s[left]
16                left += 1
17                right -= 1
18        return "".join(s)
19
20