# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    a = sorted([2, 6, 6, 8, 3, 3, 3, 3, 3, 3, 89, 89])
    l1 = ListNode(None)
    l1_c = l1
    for i in a[:6]:
        l1.next = ListNode(i)
        l1 = l1.next
    cc = ListNode(a[6])
    l1.next = cc
    l1 = l1.next
    l1.next = ListNode(a[7])
    l1 = l1.next
    l1.next = cc

    re = Solution().hasCycle(l1_c)
    print(re)