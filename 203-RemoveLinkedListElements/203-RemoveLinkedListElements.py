# Last updated: 23/12/2025, 23:29:37
1class Solution(object):
2    def removeElements(self, head, val):
3        while head and head.val == val:
4            head = head.next
5
6        curr = head
7        while curr and curr.next:
8            if curr.next.val == val:
9                curr.next = curr.next.next
10            else:
11                curr = curr.next
12
13        return head
14