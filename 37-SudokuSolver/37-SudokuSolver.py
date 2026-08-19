# Last updated: 19/08/2026, 22:47:30
1class Solution(object):
2    def solveSudoku(self, board):
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]
6
7        for r in range(9):
8            for c in range(9):
9                if board[r][c] != ".":
10                    ch = board[r][c]
11                    rows[r].add(ch)
12                    cols[c].add(ch)
13                    boxes[(r // 3) * 3 + (c // 3)].add(ch)
14
15        def findEmpty():
16            best = None
17            bestOptions = None
18            for r in range(9):
19                for c in range(9):
20                    if board[r][c] == ".":
21                        boxIndex = (r // 3) * 3 + (c // 3)
22                        options = [ch for ch in "123456789"
23                                   if ch not in rows[r]
24                                   and ch not in cols[c]
25                                   and ch not in boxes[boxIndex]]
26                        if best is None or len(options) < len(bestOptions):
27                            best = (r, c, options)
28                            bestOptions = options
29            return best
30
31        def backtrack():
32            cell = findEmpty()
33            if not cell:
34                return True
35            r, c, options = cell
36            boxIndex = (r // 3) * 3 + (c // 3)
37            for ch in options:
38                board[r][c] = ch
39                rows[r].add(ch)
40                cols[c].add(ch)
41                boxes[boxIndex].add(ch)
42                if backtrack():
43                    return True
44                board[r][c] = "."
45                rows[r].remove(ch)
46                cols[c].remove(ch)
47                boxes[boxIndex].remove(ch)
48            return False
49
50        backtrack()
51