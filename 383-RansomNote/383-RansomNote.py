# Last updated: 20/08/2026, 21:52:12
1from collections import Counter
2class Solution(object):
3    def canConstruct(self, ransomNote, magazine):
4        """
5        :type ransomNote: str
6        :type magazine: str
7        :rtype: bool
8        """
9        ransom_count = Counter(ransomNote)
10        magazine_count = Counter(magazine)
11        for ch in ransom_count:
12            if ransom_count[ch] > magazine_count[ch]:
13                return False
14        return True