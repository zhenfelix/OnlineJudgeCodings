# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def findTarget(self, root: TreeNode, k: int) -> bool:
#         arr = []
#         def inorder(root):
#             if root == None:
#                 return
#             inorder(root.left)
#             arr.append(root.val)
#             inorder(root.right)
#             return
#         inorder(root)
#         l, r = 0, len(arr)-1
#         while l<r:
#             if arr[l]+arr[r]==k:
#                 return True
#             if arr[l]+arr[r]<k:
#                 l+=1
#             else:
#                 r-=1
#         return False

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        discovered = set()
        
        return self.find(root, k, discovered)
    def find(self, root, k, discovered):
        if root is None:
            return False
        
        if self.find(root.left, k, discovered):
            return True
        
        if k - root.val in discovered:
            return True
        
        discovered.add(root.val)
        if self.find(root.right, k, discovered):
            return True
        
        return False