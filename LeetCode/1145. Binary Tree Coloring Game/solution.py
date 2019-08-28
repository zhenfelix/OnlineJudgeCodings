# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#     def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
#         def findNode(node, t):
#             if node:
#                 if node.val == t:
#                     return node
#                 ans = findNode(node.left, t)
#                 if ans:
#                     return ans
#                 return findNode(node.right, t)
#             return None
        
#         def countNode(node):
#             if not node:
#                 return 0
#             return 1 + countNode(node.left) + countNode(node.right)
        
#         if root.val == x:
#             return countNode(root.left) > n//2 or countNode(root.right) > n//2
        
#         red = findNode(root, x)
#         return countNode(red) <= n//2 or countNode(red.left) > n//2 or countNode(red.right) > n//2

    def btreeGameWinningMove(self, root, n, x):
        c = [0, 0]
        def count(node):
            if not node: return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                c[0], c[1] = l, r
            return l + r + 1
        return count(root) / 2 < max(max(c), n - sum(c) - 1)