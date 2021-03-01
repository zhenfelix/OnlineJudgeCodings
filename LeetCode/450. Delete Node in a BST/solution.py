# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if root.val == key:
            left = self.findMax(root.left)
            if left:
                left.right = root.right
                if left != root.left:
                    left.left = root.left
                root = left
            else:
                root = root.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right,key)
        return root
    
    def findMax(self, root):
        if root and root.right:
            if root.right:
                right = self.findMax(root.right)
                if right == root.right:
                    root.right = right.left
                return right

        return root