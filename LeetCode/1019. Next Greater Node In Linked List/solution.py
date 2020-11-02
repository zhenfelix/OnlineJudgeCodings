# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def nextLargerNodes(self, head: ListNode) -> List[int]:
    #     ans, st = [], [float('inf')]
    #     while head:
    #         ans.append(head.val)
    #         head = head.next 
    #     n = len(ans)
    #     for i in range(n)[::-1]:
    #         while ans[i] >= st[-1]:
    #             st.pop()
    #         tmp = st[-1]
    #         st.append(ans[i])
    #         ans[i] = tmp
    #     return [x if x < float('inf') else 0 for x in ans]
    
    def nextLargerNodes(self, head):
        res, stack = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append([len(res), head.val])
            res.append(0)
            head = head.next
        return res