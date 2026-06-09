# Last updated: 09/06/2026, 15:35:23
1class Solution(object):
2    def mergeAlternately(self, word1, word2):
3
4        result = ""
5
6        n = min(len(word1), len(word2))
7
8        for i in range(n):
9            result += word1[i]
10            result += word2[i]
11
12        result += word1[n:]
13        result += word2[n:]
14
15        return result