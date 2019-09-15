# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root: return []
#         res = []
#         stack = [(root, False)]
#         while stack:
#             cur, expanded = stack.pop()
#             if expanded:
#                 res.append(cur.val)
#                 if cur.right:
#                     stack.append((cur.right, False))
#             else:
#                 stack.append((cur, True))
#                 if cur.left:
#                     stack.append((cur.left, False))
#         return res

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res