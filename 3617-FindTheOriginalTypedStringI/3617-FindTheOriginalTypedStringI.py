# Last updated: 09/09/2025, 14:16:52
class Solution:
    def possibleStringCount(self, word):
        total = 1  
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            group_len = j - i
            total += (group_len - 1) 
            i = j
        return total
