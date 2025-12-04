# Last updated: 04/12/2025, 13:47:10
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def deleteDuplicates(self, head):
8        """
9        :type head: Optional[ListNode]
10        :rtype: Optional[ListNode]
11        """
12        curr = head
13        while curr:
14
15             while curr.next and curr.next.val == curr.val:
16
17                curr.next = curr.next.next
18             curr = curr.next
19        return head