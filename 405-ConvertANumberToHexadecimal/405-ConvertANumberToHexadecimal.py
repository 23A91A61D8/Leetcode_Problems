# Last updated: 30/06/2026, 21:43:19
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            num += 1 << 32
        hex_chars = "0123456789abcdef"
        result = []
        while num > 0:
            remainder = num % 16
            result.append(hex_chars[remainder])
            num //= 16
        return "".join(reversed(result))
