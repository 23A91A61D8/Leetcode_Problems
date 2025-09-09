# Last updated: 09/09/2025, 14:17:13
class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = 0
        for sentence in sentences:
            word_count = len(sentence.split())  
            max_words = max(max_words, word_count)
        return max_words
