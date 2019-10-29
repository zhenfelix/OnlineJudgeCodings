# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    global tail

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        global tail
        if m > 1:
            head.next = self.reverseBetween(head.next, m-1, n-1)
            return head
        if n == 1:
            tail = head.next
            return head
        phead = self.reverseBetween(head.next, m-1, n-1)
        head.next.next = head
        if m == 1:
            head.next = tail
        return phead
