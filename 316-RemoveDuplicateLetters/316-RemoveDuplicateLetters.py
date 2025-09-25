# Last updated: 25/09/2025, 22:00:23
class Solution(object):
    def removeDuplicateLetters(self, s):
        last_index = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and last_index[stack[-1]] > i:
                    seen.remove(stack.pop())
                stack.append(c)
                seen.add(c)
        return "".join(stack)
