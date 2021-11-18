# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre, cur = dummy, head
        sz = 0
        while cur:
            sz += 1
            cnt = 0
            tail = cur
            pt = pre
            for i in range(sz):
                pt = pt.next
                tail = tail.next
                cnt += 1
                if not tail:
                    break
            if cnt&1:
                cur = tail
                pre = pt 
            else:
                tmp = pre
                while cur != tail:
                    nxt = cur.next
                    cur.next = pre
                    pre = cur
                    cur = nxt
                tt = tmp.next
                tmp.next = pre
                pre = tt
                pre.next = cur

        return dummy.next
                

