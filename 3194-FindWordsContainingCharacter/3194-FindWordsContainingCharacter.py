# Last updated: 09/09/2025, 14:17:04
class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        return result
