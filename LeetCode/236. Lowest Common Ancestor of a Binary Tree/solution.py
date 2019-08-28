# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(cur):
            if not cur or cur == p or cur == q:
                return cur
            left, right = dfs(cur.left), dfs(cur.right)
            if not left:
                return right
            elif not right:
                return left
            else:
                return cur
        return dfs(root)