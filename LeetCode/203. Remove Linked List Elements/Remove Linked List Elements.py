# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        result = head
        while head and head.val == val:
            result = head.next
            head = head.next
        while head:
            while head.next and head.next.val == val:
                head.next = head.next.next
            head = head.next
        return result
