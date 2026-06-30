# Last updated: 30/06/2026, 21:44:18
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        while curr:

             while curr.next and curr.next.val == curr.val:

                curr.next = curr.next.next
             curr = curr.next
        return head