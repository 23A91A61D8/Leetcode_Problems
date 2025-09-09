# Last updated: 09/09/2025, 22:13:47
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for c1, c2 in zip(s, t):
         
            if c1 in map_s_t and map_s_t[c1] != c2:
                return False
            if c2 in map_t_s and map_t_s[c2] != c1:
                return False

            map_s_t[c1] = c2
            map_t_s[c2] = c1

        return True
