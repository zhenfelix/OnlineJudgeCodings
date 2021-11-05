# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [-float('inf')]
        def dfs(cur):
            if not cur:
                return 0
            left, right = dfs(cur.left), dfs(cur.right)
            res[0] = max(res[0], max(0,left)+cur.val+max(0,right))
            return max(cur.val,left+cur.val,right+cur.val)
        dfs(root)
        return res[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -float('inf')

        def dfs(cur):
            nonlocal res
            if not cur:
                return 0
            sums = cur.val
            lsums = max(0,dfs(cur.left))
            rsums = max(0,dfs(cur.right))
            res = max(res, sums+lsums+rsums)
            return sums+max(lsums,rsums)
        dfs(root)
        return res