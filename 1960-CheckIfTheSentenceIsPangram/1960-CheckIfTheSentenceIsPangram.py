# Last updated: 30/06/2026, 21:41:22
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        letters = set()
        for ch in sentence:
            if ch.isalpha():
                letters.add(ch.lower())
        return len(letters) == 26        