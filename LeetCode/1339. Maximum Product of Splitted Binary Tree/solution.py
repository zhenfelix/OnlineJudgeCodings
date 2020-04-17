# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def dfs1(cur):
            if not cur:
                return 0
            cur.val += dfs1(cur.left) + dfs1(cur.right)
            return cur.val
        
        def dfs2(cur):
            if not cur:
                return 0
            return min([cur.val,dfs2(cur.left),dfs2(cur.right)],key=lambda x:abs(sums-2*x))
        
        sums = dfs1(root)
        res = dfs2(root)
        return ((sums-res)*res)%(10**9+7)
            
                