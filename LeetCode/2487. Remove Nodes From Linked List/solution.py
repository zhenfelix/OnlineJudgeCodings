# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nxt = self.removeNodes(head.next)
        if not nxt or head.val >= nxt.val:
            head.next = nxt
            return head
        return nxt



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        st = []
        while arr:
            v = arr.pop()
            if not st or v >= st[-1]:
                st.append(v)
        cur = dummy = ListNode()
        while st:
            v = st.pop()
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

