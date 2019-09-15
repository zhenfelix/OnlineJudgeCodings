# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def kthSmallest(self, root: TreeNode, k: int) -> int:
#         def preorder(node):
#             if node:
#                 if preorder(node.left):
#                     return True
#                 if idx[0] == k:
#                     ans[0] = node.val
#                     return True
#                 idx[0] += 1
#                 if preorder(node.right):
#                     return True
#             return False
#         ans = [-1]
#         idx = [1]
#         preorder(root)
#         return ans[0]
        

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root or not k: return None
        
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        
        while stack:
            node = stack.pop()
            k -= 1
            if k == -1: return node.val
            node = node.right
            while node:
                stack.append(node)
                node = node.left