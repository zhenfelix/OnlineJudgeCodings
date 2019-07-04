# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# import heapq
## heapq with custom compare predicate
## https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         ans= ListNode(-1)
#         cur = ans
#         hq = []
#         cc = 0
#         for node in lists:
#             if node:
#                 heapq.heappush(hq, (node.val,cc,node))#Line 15: TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
#                 cc += 1
            

#         # hq = [(node.val, node) for node in lists]
#         # heapq.heapify(hq)
#         while len(hq) > 0:
#             cur.next = heapq.heappop(hq)[-1]
#             cur = cur.next
#             if cur.next:
#                 heapq.heappush(hq, (cur.next.val, cc, cur.next))
#                 cc += 1
#         return ans.next
        
# from Queue import PriorityQueue

# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         head = point = ListNode(0)
#         q = PriorityQueue()
#         for l in lists:
#             if l:
#                 q.put((l.val, l))
#         while not q.empty():
#             val, node = q.get()
#             point.next = ListNode(val)
#             point = point.next
#             node = node.next
#             if node:
#                 q.put((node.val, node))
#         return head.next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
