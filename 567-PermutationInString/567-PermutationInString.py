# Last updated: 30/06/2026, 21:43:15
class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        count_s1 = [0] * 26
        for c in s1:
            count_s1[ord(c) - ord('a')] += 1

        window = [0] * 26
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        if window == count_s1:
            return True

        for i in range(len(s1), len(s2)):
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1
            window[ord(s2[i]) - ord('a')] += 1
            if window == count_s1:
                return True

        return False
