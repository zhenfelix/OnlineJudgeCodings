# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
#         cur = TreeNode(None)
#         cur.right = root 
#         flag = False
#         st = [cur]
#         while st:
#             cur = st.pop()
#             if flag: return cur 
#             if cur == p: flag = True
#             if cur.right:
#                 st.append(cur.right)
#                 cur = cur.right
#                 while cur.left: 
#                     st.append(cur.left)
#                     cur = cur.left
#         return None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     # dummy = TreeNode(float('inf'))
#     def inorderSuccessor(self, root: TreeNode, p: TreeNode, right = None) -> TreeNode:
#         if not root: return right
#         if p.val >= root.val:
#             return self.inorderSuccessor(root.right,p,right)
#         else:
#             return self.inorderSuccessor(root.left,p,root)

class Solution:
    
    def inorderSuccessor(self, root: TreeNode, p: TreeNode, right = None) -> TreeNode:
        res = None
        cur = root
        while cur:
            if cur.val <= p.val:
                cur = cur.right
            else:
                res = cur
                cur = cur.left
        return res



        