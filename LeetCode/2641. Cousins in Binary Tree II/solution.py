# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tot = []
        def dfs(cur,d):
            if d == len(tot):
                tot.append(0)
            tot[d] += cur.val 
            if cur.left: dfs(cur.left,d+1)
            if cur.right: dfs(cur.right,d+1)
            return 
        dfs(root,0)
        def dfs2(cur,d,cousin):
            cur.val = tot[d]-cousin
            s = 0
            if cur.left: s += cur.left.val 
            if cur.right: s += cur.right.val 
            if cur.left: dfs2(cur.left,d+1,s)
            if cur.right: dfs2(cur.right,d+1,s)
            return
        dfs2(root,0,root.val)
        return root