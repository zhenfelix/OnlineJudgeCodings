# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(cur, mi, mx):
            nonlocal ans 
            if not cur:
                return  
            val = cur.val 
            mi = min(mi, val)
            mx = max(mx, val)
            ans = max(ans, abs(mx-val))
            ans = max(ans, abs(mi-val))
            dfs(cur.left, mi, mx)
            dfs(cur.right, mi, mx)
            return
        dfs(root,inf,-inf)
        return ans 

