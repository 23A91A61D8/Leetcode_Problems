# Last updated: 01/10/2026, 21:02:39
1class Solution(object):
2    def isValid(self, s):
3        stack = []
4        pairs = {
5            ')': '(',
6            ']': '[',
7            '}': '{'
8        }
9        for ch in s:
10            if ch in pairs:
11                if not stack or stack.pop() != pairs[ch]:
12                    return False
13            else:
14                stack.append(ch)
15        return len(stack) == 0
16