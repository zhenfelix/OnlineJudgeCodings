# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def check(cur, k):
            for _ in range(k):
                if not cur:
                    return False
                cur = cur.next
            return True
        def reverse(cur, pre, k):
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return cur, pre
        dummy = ListNode()
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if not check(cur, k):
                break
            tmp = pre
            cur, pre = reverse(cur, pre, k)
            tmp.next.next = cur
            tmp.next, pre = pre, tmp.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rev(self, h):
        tmp = h.next
        if not tmp:
            return h
        new_h = self.rev(tmp)
        tmp.next = h
        h.next = None
        return new_h
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        pre = None
        for i in range(k):
            if cur == None:
                return head
            pre = cur
            cur = cur.next
        pre.next = None
        new_head = self.rev(head)
        head.next = self.reverseKGroup(cur, k)
        return new_head