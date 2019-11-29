# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()
        return

# class Solution:
#     def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
#         n = 0
#         cur = head
#         while cur:
#             n += 1
#             cur = cur.getNext()
#         while n:
#             n -= 1
#             cur = head
#             for i in range(n):
#                 cur = cur.getNext()
#             cur.printValue()
#         return
        

# - [Print out an immutable singly linked list in reverse](https://leetcode.com/discuss/interview-question/124617/Print-out-an-immutable-singly-linked-list-in-reverse/)