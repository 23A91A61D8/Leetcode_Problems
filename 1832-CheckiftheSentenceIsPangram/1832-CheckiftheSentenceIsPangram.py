# Last updated: 19/06/2026, 22:22:59
1class Solution(object):
2    def checkIfPangram(self, sentence):
3        """
4        :type sentence: str
5        :rtype: bool
6        """
7        letters = set()
8        for ch in sentence:
9            if ch.isalpha():
10                letters.add(ch.lower())
11        return len(letters) == 26        