# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         cnt = 0
#         cur = head
#         while cur:
#             cnt += 1
#             cur = cur.next
#         cnt //= 2
#         dummy = ListNode()
#         dummy.next = head
#         cur = head
#         pre = dummy
#         for _ in range(cnt):
#             cur = cur.next
#             pre = pre.next
#         pre.next = cur.next
#         return dummy.next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head.next==None):return None 
        tortoise=head
        rabbit=head
        follow_tortoise=None
        while(rabbit and rabbit.next):
            follow_tortoise=tortoise
            tortoise=tortoise.next
            rabbit=rabbit.next.next
        follow_tortoise.next=tortoise.next
        return head