# Last updated: 09/09/2025, 14:16:55
class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []

        for char in s:
            if char.islower():
                result.append(char)
            elif char == '*':
                if result:
                    result.pop()  
            elif char == '#':
                result += result  
            elif char == '%':
                result.reverse()  

        return ''.join(result)
