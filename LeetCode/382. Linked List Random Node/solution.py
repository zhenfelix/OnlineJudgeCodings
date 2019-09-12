# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random

# class Solution:

#     def __init__(self, head: ListNode):
#         """
#         @param head The linked list's head.
#         Note that the head is guaranteed to be not null, so it contains at least one node.
#         """
#         self.head = head
        

#     def getRandom(self) -> int:
#         """
#         Returns a random node's value.
#         """
#         cur = self.head
#         idx = 1
#         res = None
#         while cur:
#             if random.randint(1,idx) == 1:
#                 res = cur.val
#             cur = cur.next
#             idx += 1
#         return res

class Solution(object):

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        node = self.head
        before = 0
        buffer = [None] * 100
        while node:
            now = 0
            while node and now < 100:
                buffer[now] = node
                node = node.next
                now += 1
            r = random.randrange(now + before)
            if r < now:
                pick = buffer[r]
            before += now
        return pick.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()