# Last updated: 12/09/2025, 19:16:48
class Solution(object):
    def numberOfLines(self, widths, s):
        lines = 1
        current_width = 0
        for char in s:
            w = widths[ord(char) - ord('a')]
            if current_width + w > 100:
                lines += 1
                current_width = w
            else:
                current_width += w
        return [lines, current_width]
