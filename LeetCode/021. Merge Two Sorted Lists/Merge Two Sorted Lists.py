# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(None)
        l = result
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        l.next = l1 or l2
        return result.next


if __name__ == "__main__":
    a = sorted([2, 6, 8, 3, 89])
    b = sorted([4, 8, 5, 11, 32, 101, 36])
    l1 = ListNode(None)
    l1_o = l1
    l2 = ListNode(None)
    l2_o = l2
    for i in a:
        l1.next = ListNode(i)
        l1 = l1.next
    for i in b:
        l2.next = ListNode(i)
        l2 = l2.next

    re = Solution().mergeTwoLists(l1_o.next, l2_o.next)
    while re:
        print(re.val)
        re = re.next


