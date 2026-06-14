# Last updated: 14/06/2026, 21:57:10
1class Solution(object):
2    def wordPattern(self, pattern, s):
3        words = s.split()
4        if len(pattern) != len(words):
5            return False
6
7        mapping = {}
8        used = set()
9
10        for c, w in zip(pattern, words):
11            if c in mapping:
12                if mapping[c] != w:
13                    return False
14            else:
15                if w in used:
16                    return False
17                mapping[c] = w
18                used.add(w)
19
20        return True
21