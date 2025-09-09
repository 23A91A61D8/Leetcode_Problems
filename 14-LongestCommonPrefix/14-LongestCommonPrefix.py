# Last updated: 09/09/2025, 14:20:34
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        if min_len == 0:
            return ""

        for i in range(min_len):
            ch = strs[0][i]
            for k in range(1, len(strs)):
                if strs[k][i] != ch:
                    return strs[0][:i]
        return strs[0][:min_len]
