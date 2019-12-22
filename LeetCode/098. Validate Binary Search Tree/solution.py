# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def dfs(cur, alpha, beta):
    #         if not cur:
    #             return True
    #         return alpha < cur.val < beta and dfs(cur.left, alpha, cur.val) and dfs(cur.right, cur.val, beta)

    #     return dfs(root, -float("inf"), float("inf"))


    def isValidBST(self, root, left = float('-inf'), right = float('inf')):
        return not root or left < root.val < right and \
                self.isValidBST(root.left, left, root.val) and \
                self.isValidBST(root.right, root.val, right)