# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def deepestLeavesSum(self, root: TreeNode) -> int:
#         q = collections.deque()
#         q.append(root)
#         res = 0
#         while q:
#             n = len(q)
#             res = 0
#             for _ in range(n):
#                 cur = q.popleft()
#                 res += cur.val
#                 if cur.left:
#                     q.append(cur.left)
#                 if cur.right:
#                     q.append(cur.right)
#         return res



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root):
        l = [root]
        while l:
            pre, l = l, [child for p in l for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)
