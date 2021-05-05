# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from functools import lru_cache
class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:
        @lru_cache(None)
        def dfs(cur, remain):
            if not cur:
                return 0
            res = dfs(cur.left,k) + dfs(cur.right,k)
            for r in range(remain):
                res = max(res, dfs(cur.left,r)+dfs(cur.right,remain-1-r)+cur.val)
            # print(cur,remain,res)
            return res 
        return dfs(root,k)

