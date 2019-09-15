# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
#         def preorder(node):
#             if not node:
#                 return
#             preorder(node.left)
#             arr.append((node.val,node))
#             preorder(node.right)
        
#         def lower_bound(target):
#             left, right = 0, len(arr)-1
#             while left <= right:
#                 mid = (left+right)//2
#                 if arr[mid][0] <= target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             return left
        
#         arr = []
#         preorder(root)
#         idx = lower_bound(p.val)
#         if idx == len(arr):
#             return None
#         return arr[idx][1]

# class Solution:
#     def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
#         parent, child = [None], None
#         def up(cur, pa):
#             # print(cur.val, parent)
#             if cur.val == p.val:
#                 return
#             if cur.val < p.val:
#                 up(cur.right, pa)
#             else:
#                 pa[0] = cur
#                 up(cur.left, pa)
#             return
        
#         child = p.right
#         while child and child.left:
#             child = child.left
#         if child:
#             return child
#         up(root, parent)
#         return parent[0]


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = None
        while root:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res
        