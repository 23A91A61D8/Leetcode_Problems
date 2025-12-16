# Last updated: 16/12/2025, 22:39:03
1class Solution(object):
2    def hasCycle(self, head):
3        """
4        :type head: ListNode
5        :rtype: bool
6        """
7        slow = head
8        fast = head
9
10        while fast and fast.next:
11            slow = slow.next
12            fast = fast.next.next
13
14            if slow == fast:
15                return True
16
17        return False
18