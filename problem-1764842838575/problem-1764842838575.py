# Last updated: 04/12/2025, 15:37:18
1class Solution(object):
2    def deleteDuplicates(self, head):
3        dummy = ListNode(0, head)
4        prev = dummy
5        curr = head
6
7        while curr:
8            if curr.next and curr.val == curr.next.val:
9                while curr.next and curr.val == curr.next.val:
10                    curr = curr.next
11                prev.next = curr.next
12            else:
13                prev = prev.next
14            curr = curr.next
15
16        return dummy.next
17