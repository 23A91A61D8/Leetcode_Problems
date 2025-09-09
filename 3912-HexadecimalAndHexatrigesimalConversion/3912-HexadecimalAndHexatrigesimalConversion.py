# Last updated: 09/09/2025, 14:16:53
class Solution(object):
    def concatHex36(self, n):
        """
        :type n: int
        :rtype: str
        """
        hex_val = format(n * n, 'X')    
        base36_val = format(n * n * n, 'X') 
        def to_base36(num):
            chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            while num > 0:
                result = chars[num % 36] + result
                num //= 36
            return result or "0"

        base36_val = to_base36(n * n * n)
        return hex_val + base36_val
