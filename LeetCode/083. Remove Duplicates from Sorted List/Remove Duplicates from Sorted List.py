# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head = head.next
        return result


if __name__ == "__main__":
    a = sorted([2, 6, 6, 8, 3, 3, 3, 3, 3, 3, 89, 89])
    l1 = ListNode(None)
    l1_c = l1
    for i in a:
        l1.next = ListNode(i)
        l1 = l1.next

    re = Solution().deleteDuplicates(l1_c)
    while re:
        print(re.val)
        re = re.next