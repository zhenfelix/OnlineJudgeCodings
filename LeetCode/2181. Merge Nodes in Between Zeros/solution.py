# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        cur = 0
        while head:
            if head.val == 0:
                if cur > 0:
                    tail.next = ListNode(cur)
                    tail = tail.next 
                cur = 0
            else:
                cur += head.val
            head = head.next
        return dummy.next