# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def find(cur, val):
            if not cur:
                return False
            if cur.val == val:
                return True
            elif cur.val < val:
                return find(cur.right, val)
            else:
                return find(cur.left, val)
            
        def preorder(root):
            if not root:
                return False
            if find(root2, target - root.val):
                return True
            return preorder(root.left) or preorder(root.right)
        
        return preorder(root1)

# class Solution(object):
#     def twoSumBSTs(self, root1, root2, target):
#         ans1 = []
#         def dfs1(node):
#             if node:
#                 dfs1(node.left)
#                 ans1.append(node.val)
#                 dfs1(node.right)
#         ans2 = []
#         def dfs2(node):
#             if node:
#                 dfs2(node.left)
#                 ans2.append(node.val)
#                 dfs2(node.right)
#         dfs1(root1)
#         dfs2(root2)
#         seen = set(ans1)
#         for x in ans2:
#             if target-x in seen:
#                 return True
#         return False
            