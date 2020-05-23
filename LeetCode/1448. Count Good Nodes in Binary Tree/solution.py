# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def dfs(cur, mx):
            nonlocal cnt
            if not cur:
                return
            if cur.val >= mx:
                cnt += 1
                mx = cur.val
            dfs(cur.left,mx)
            dfs(cur.right,mx)
        dfs(root,-float('inf'))
        return cnt

    def goodNodes(self, r, ma=-10000):
        return self.goodNodes(r.left, max(ma, r.val)) + self.goodNodes(r.right, max(ma, r.val)) + (r.val >= ma) if r else 0

