# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def isMirrior(left, right):
#             if left == None and right == None:
#                 return True
#             if left == None or right == None:
#                 return False
#             if left.val != right.val:
#                 return False
#             if not isMirrior(left.left, right.right):
#                 return False
#             if not isMirrior(left.right, right.left):
#                 return False
#             return True
#         return not root or isMirrior(root.left, root.right)

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root is None:
#             return True
        
#         return self.isSymmetricRecu(root.left, root.right)
    
#     def isSymmetricRecu(self, left, right):
#         if left is None and right is None:
#             return True
#         if left is None or right is None or left.val != right.val:
#             return False
#         return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)        

from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = deque()       
        q.append(root.left)
        q.append(root.right)
        while len(q) > 0:
            left = q.popleft()
            right = q.popleft()
            if left == None and right == None:
                continue
            if left == None or right == None or left.val != right.val:
                return False
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)
        return True