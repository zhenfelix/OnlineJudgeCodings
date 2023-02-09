# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left: root.left = TreeNode(-1, left = self.expandBinaryTree(root.left))
        if root.right: root.right = TreeNode(-1, right = self.expandBinaryTree(root.right))
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(cur, parent, isleft):
            if not cur:
                return
            if cur != parent:
                if isleft:
                    parent.left = TreeNode(-1)
                    parent.left.left = cur
                else:
                    parent.right = TreeNode(-1)
                    parent.right.right = cur 
            dfs(cur.left, cur, True)
            dfs(cur.right, cur, False)
            return 

        dfs(root, root, True)
        return root
