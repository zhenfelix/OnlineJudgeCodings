"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
# class Solution:
#     def inorderSuccessor(self, node: 'Node') -> 'Node':
#         cur, res = node, None
#         while cur:
#             if cur.val > node.val:
#                 res = cur
#                 cur = cur.left
#             else:
#                 cur = cur.right
#         if res:
#             return res
#         res = node
#         while res and res.val <= node.val:
#             res = res.parent
#         return res

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        res = node
        if not res:
            pass
        elif res.right:
            res = res.right
            while res.left:
                res = res.left
        else:
            while res and res.val <= node.val:
                res = res.parent
        return res