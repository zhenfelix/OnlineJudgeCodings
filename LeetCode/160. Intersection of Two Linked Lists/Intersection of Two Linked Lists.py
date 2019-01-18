# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        headA_c1 = headA
        while headA_c1:
            lenA += 1
            headA_c1 = headA_c1.next
        lenB = 0
        headB_c1 = headB
        while headB_c1:
            lenB += 1
            headB_c1 = headB_c1.next
        headA_c2 = headA
        headB_c2 = headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                headA_c2 = headA_c2.next
        elif lenA < lenB:
            for i in range(lenB-lenA):
                headB_c2 = headB_c2.next
        while headA_c2 and headB_c2:
            if headA_c2 == headB_c2:
                return headA_c2
            headB_c2 = headB_c2.next
            headA_c2 = headA_c2.next
        return None

