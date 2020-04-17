# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(cur):
            if not cur:
                return 0, 0, 0
            ll, lr, lh = dfs(cur.left)
            rl, rr, rh = dfs(cur.right)
            return lr+1, rl+1, max(lr+1,rl+1,lh,rh)
        return dfs(root)[-1]-1