# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(cur,parent,grandparent):
            if not cur:
                return 0
            sums = 0
            if grandparent:
                sums += cur.val
            grandparent, parent = parent, cur.val%2 == 0
            sums += dfs(cur.left,parent,grandparent)
            sums += dfs(cur.right,parent,grandparent)
            return sums
        return dfs(root,False,False)


class Solution:
    def sumEvenGrandparent(self, root, p=1, gp=1):
        return self.sumEvenGrandparent(root.left, root.val, p) \
            + self.sumEvenGrandparent(root.right, root.val, p) \
            + root.val * (1 - gp % 2) if root else 0