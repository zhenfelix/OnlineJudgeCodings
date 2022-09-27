# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def minSupplyStationNumber(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dfs(cur, s, p):
            if not cur:
                return 0 if (s == 0) else float('inf')
            if s == 0 and p == 0:
                return min(dfs(cur.left,0,s)+dfs(cur.right,1,s), dfs(cur.left,1,s)+dfs(cur.right,0,s), dfs(cur.left,1,s)+dfs(cur.right,1,s))
            else:
                return min(dfs(cur.left,0,s),dfs(cur.left,1,s)) + min(dfs(cur.right,1,s),dfs(cur.right,0,s))+s
            
        # print(dfs(root,0,1),dfs(root,1,1),dfs(root,0,0),dfs(root,1,0))
        return min(dfs(root,0,0),dfs(root,1,0))