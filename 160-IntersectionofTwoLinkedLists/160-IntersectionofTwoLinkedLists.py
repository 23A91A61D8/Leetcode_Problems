# Last updated: 02/01/2026, 21:51:37
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution(object):
8    def getIntersectionNode(self, headA, headB):
9        """
10        :type head1, head1: ListNode
11        :rtype: ListNode
12        """
13        if not headA or not headB:
14            return None
15        listA = headA
16        listB = headB
17        while listA != listB:
18            listA = listA.next if listA else headB
19            listB = listB.next if listB else headA
20        return listA
21
22        