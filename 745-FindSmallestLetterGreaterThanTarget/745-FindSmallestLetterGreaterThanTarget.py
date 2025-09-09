# Last updated: 09/09/2025, 14:18:44
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for ch in letters:
            if ch > target:
                return ch
        return letters[0]
