# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pos = []
        left = head
        cur = left.next
        right = cur.next
        p = 1
        while right:
            p += 1
            if (left.val < cur.val and cur.val > right.val) or (left.val > cur.val and cur.val < right.val):
                pos.append(p)
            left = cur
            cur = right
            right = right.next
        if len(pos) < 2:
            return [-1,-1]
        return [min(b-a for a,b in zip(pos,pos[1:])), pos[-1]-pos[0]]
