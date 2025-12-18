# Last updated: 18/12/2025, 22:45:59
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def reverseList(self, head):
8        """
9        :type head: Optional[ListNode]
10        :rtype: Optional[ListNode]
11        """
12        prev = None
13        curr = head
14        while curr:
15            next_node = curr.next
16            curr.next = prev
17            prev = curr
18            curr = next_node
19        return prev
20        