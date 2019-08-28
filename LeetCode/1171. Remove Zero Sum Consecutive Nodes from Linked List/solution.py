# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def removeZeroSumSublists(self, head: ListNode) -> ListNode:
#         dummy = ListNode(0)
#         dummy.next, pre = head, dummy
#         mp = {0 :dummy}
#         while head:
#             head.val += pre.val
#             if head.val not in mp:
#                 mp[head.val] = head
#                 pre = head
#             else:
#                 pre = mp[head.val]
#                 tmp = pre.next
#                 while tmp != head:
#                     del mp[tmp.val]
#                     tmp = tmp.next
#                 pre.next = head.next
#             head = head.next
            
#         head, pre = dummy.next, dummy
#         # print(head)
#         def dfs(cur, val):
#             if not cur:
#                 return
#             dfs(cur.next, cur.val)
#             cur.val -= val
#             return
        
#         dfs(dummy.next, 0)
#         return dummy.next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        hmap = {0: dummy}

        node, cumsum = head, 0
        while node:
            nex = node.next
            cumsum += node.val
            if cumsum in hmap:
                temp = hmap[cumsum]
                delnode = temp.next
                temp.next = node.next

                tcsum = cumsum
                while delnode != node:
                    tcsum += delnode.val
                    del hmap[tcsum]
                    delnode = delnode.next
            else:
                hmap[cumsum] = node
            node = nex
        return dummy.next
            
            
            