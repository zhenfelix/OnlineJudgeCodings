# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def recoverTree(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         def dfs(left, right, cur):
#             if not cur:
#                 return
#             if cur.val > right.val:
#                 cur.val, right.val = right.val, cur.val
#             if cur.val < left.val:
#                 cur.val, left.val = left.val, cur.val
#             dfs(left, cur, cur.left)
#             dfs(cur, right, cur.right)
#         dfs(TreeNode(-float("inf")),TreeNode(float("inf")),root)

# class Solution:
#     def recoverTree(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         def dfs(alpha, beta, cur):
#             if not cur:
#                 return cur

#             left, right = dfs(alpha, cur.val, cur.left), dfs(cur.val, beta, cur.right)
#             if left and right:
#                 left.val, right.val = right.val, left.val
#                 return None
#             if left:
#                 if alpha < left.val < beta:
#                     left.val, cur.val = cur.val, left.val
#                     return None
#                 return left
#             if right:
#                 if alpha < right.val < beta:
#                     right.val, cur.val = cur.val, right.val
#                     return None
#                 return right
#             if cur.val < alpha or cur.val > beta:
#                 return cur
#             return None
#         dfs(-float("inf"),float("inf"),root)


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pointers = [TreeNode(-float("inf")), None, None]
        def dfs(cur):
            if not cur:
                return 
            dfs(cur.left)
            if pointers[1] == None and pointers[0].val > cur.val:
                pointers[1] = pointers[0]
            if pointers[1] != None and pointers[0].val > cur.val:
                pointers[2] = cur
            pointers[0] = cur
            dfs(cur.right)
            return 
        dfs(root)
        pointers[1].val, pointers[2].val = pointers[2].val, pointers[1].val
        return