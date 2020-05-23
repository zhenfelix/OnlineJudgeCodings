# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        left = right = head
        for _ in range(k):
            right = right.next
        while right:
            right = right.next
            left = left.next
        return left