# Last updated: 30/06/2026, 21:41:27
class Solution(object):
    def mergeAlternately(self, word1, word2):

        result = ""

        n = min(len(word1), len(word2))

        for i in range(n):
            result += word1[i]
            result += word2[i]

        result += word1[n:]
        result += word2[n:]

        return result