# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(cur):
            if not cur:
                return cur
            left, right = dfs(cur.left), dfs(cur.right)
            cur.left, cur.right = left, right
            if cur.val == target and (not left) and (not right):
                return None
            return cur
        return dfs(root)


class Solution(object):
    def removeLeafNodes(self, root, target):
        if root:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            if root.val != target or root.left or root.right:
                return root