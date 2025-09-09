# Last updated: 09/09/2025, 14:20:01
class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
            row.append(1)
        return row
        
