# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def convertBiNode(self, root: TreeNode) -> TreeNode:
#         def dfs(cur):
#             if not cur:
#                 return None, None
#             ll, lr = dfs(cur.left)
#             rl, rr = dfs(cur.right)
#             left = ll or cur
#             if lr: lr.right = cur
#             right = rr or cur
#             cur.right = rl
#             cur.left = None
#             return left, right

#         return dfs(root)[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def dfs(cur, pre):
            if not cur:
                return pre
            pre = dfs(cur.left, pre)
            pre.right = cur
            cur.left = None
            pre = dfs(cur.right, cur)
            return pre
        dummy = TreeNode()
        dfs(root,dummy)
        return dummy.right