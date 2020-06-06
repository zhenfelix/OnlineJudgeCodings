# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        if root.val in [p.val,q.val]:
            return root
        left, right = self.lowestCommonAncestor(root.left,p,q), self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right