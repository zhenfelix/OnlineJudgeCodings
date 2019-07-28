"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# from collections import deque

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root:
#             return root
        
        
#         q = deque()
#         q.append(root)
        
#         while(len(q) > 0):
#             n = len(q)
#             # arr = []
#             for i in range(n):
#                 a = q.popleft()
#                 if i < n-1:
#                     a.next = q[0]
#                 else:
#                     a.next = None
#                 # arr.append(a)
#                 if a.left != None:
#                     q.append(a.left)
#                 if a.right != None:
#                     q.append(a.right)
#             # for i in range(n):
#             #     if i < n-1:
#             #         arr[i].next = arr[i+1]
#             #     else:
#             #         arr[i].next = None
                    
#         return root



class Solution:
    def connect(self, root):
        tail = dummy = Node(0)
        node = root
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
            tail.next = node.right
            if tail.next:
                tail = tail.next
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next
                
        return root