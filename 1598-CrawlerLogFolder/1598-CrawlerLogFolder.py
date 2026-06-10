# Last updated: 10/06/2026, 13:02:21
1class Solution(object):
2    def minOperations(self, logs):
3
4        depth = 0
5
6        for log in logs:
7
8            if log == "../":
9
10                if depth > 0:
11                    depth -= 1
12
13            elif log == "./":
14                continue
15
16            else:
17                depth += 1
18
19        return depth