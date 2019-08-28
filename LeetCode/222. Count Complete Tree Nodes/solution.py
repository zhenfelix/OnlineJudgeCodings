# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def countNodes(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         h = 0
#         r = root
#         while r.left:
#             h += 1
#             r = r.left
        
        
#         def dfs(node, path, idx):
#             if idx == 0:
#                 return not not node
#             if path & 1<<(idx-1):
#                 return dfs(node.right, path, idx-1)
#             else:
#                 return dfs(node.left, path, idx-1)
                
#         left, right = 0, (1<<h)-1      
#         while left <= right:
#             mid = (left+right)//2
#             if dfs(root, mid, h):
#                 left = mid+1
#             else:
#                 right = mid-1
#         # print(h,right)
#         return (1<<h) + right

class Solution:
    def height(self, root):
        if not root:
            return 0
        return 1 + self.height(root.left)
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        h = self.height(root)
        if self.height(root.right) == h-1:
            return (1<<(h-1))+self.countNodes(root.right)
        else:
            return (1<<(h-2))+self.countNodes(root.left)
        