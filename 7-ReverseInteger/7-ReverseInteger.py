# Last updated: 30/06/2026, 21:44:39
class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x *= sign
        rev = int(str(x)[::-1]) * sign
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev