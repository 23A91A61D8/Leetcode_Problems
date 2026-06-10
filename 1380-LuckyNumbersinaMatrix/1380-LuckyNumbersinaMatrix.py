# Last updated: 10/06/2026, 13:00:52
1class Solution(object):
2    def luckyNumbers(self, matrix):
3
4        result = []
5
6        for row in matrix:
7
8            row_min = min(row)
9
10            col = row.index(row_min)
11
12            is_lucky = True
13
14            for r in matrix:
15
16                if r[col] > row_min:
17                    is_lucky = False
18                    break
19
20            if is_lucky:
21                result.append(row_min)
22
23        return result