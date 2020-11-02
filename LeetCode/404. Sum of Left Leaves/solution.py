# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(cur, isLeft):
            # print(cur.val)
            if not cur:
                return 0
            if (not cur.left) and (not cur.right):
                return cur.val if isLeft else 0
            left, right = dfs(cur.left,True), dfs(cur.right,False)
            return left + right
        return dfs(root, False)