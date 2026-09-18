# Last updated: 18/09/2026, 21:24:57
1class Solution(object):
2    def longestPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        count = {}
8        for ch in s:
9            count[ch] = count.get(ch, 0) + 1    
10        length = 0
11        has_odd = False
12        for freq in count.values():
13            length += (freq // 2) * 2
14            if freq % 2 == 1:
15                has_odd = True
16        if has_odd:
17            length += 1
18        return length
19