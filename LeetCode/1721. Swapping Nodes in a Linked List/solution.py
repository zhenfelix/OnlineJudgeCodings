# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        left, right, tail = head, head, head
        for _ in range(k-1):
            left = left.next
            tail = tail.next
        tail = tail.next
        while tail:
            right = right.next
            tail = tail.next
        left.val, right.val = right.val, left.val
        return head