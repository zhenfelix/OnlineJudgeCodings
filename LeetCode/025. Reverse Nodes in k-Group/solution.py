# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rev(self, h):
        tmp = h.next
        if not tmp:
            return h
        new_h = self.rev(tmp)
        tmp.next = h
        h.next = None
        return new_h
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        pre = None
        for i in range(k):
            if cur == None:
                return head
            pre = cur
            cur = cur.next
        pre.next = None
        new_head = self.rev(head)
        head.next = self.reverseKGroup(cur, k)
        return new_head