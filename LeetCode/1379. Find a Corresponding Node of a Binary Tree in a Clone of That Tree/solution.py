# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(a,b):
            if not a:
                return a
            if a == target:
                return b
            left = dfs(a.left,b.left)
            right = dfs(a.right,b.right)
            return left or right
        return dfs(original,cloned)