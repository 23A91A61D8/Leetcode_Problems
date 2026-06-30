# Last updated: 30/06/2026, 21:44:20
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return dummy.next
