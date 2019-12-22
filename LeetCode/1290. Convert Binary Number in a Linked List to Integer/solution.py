class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head: 
            ans = 2*ans + head.val 
            head = head.next 
        return ans 


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         res = []
#         while head:
#             res.append(head.val)
#             head = head.next
#         base = 1
#         ans = 0
#         for a in res[::-1]:
#             ans += a*base
#             base *= 2
#         return ans