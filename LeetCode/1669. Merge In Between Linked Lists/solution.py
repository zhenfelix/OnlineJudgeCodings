# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, h1: ListNode, a: int, b: int, h2: ListNode) -> ListNode:
        head = h1
        pre, nxt = None, None
        while a:
            pre = h1
            h1 = h1.next
            a -= 1
            b -= 1
        while b:
            h1 = h1.next
            b -= 1
        nxt = h1.next
        pre.next = h2
        while h2.next:
            h2 = h2.next
        h2.next = nxt
        return head