# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def maxSumBST(self, root: TreeNode) -> int:
#         def dfs(cur):
#             nonlocal res
#             sums_l, f_l, left_l, right_l = 0, True, cur.val, -float('inf')
#             if cur.left:
#                 sums_l, f_l, left_l, right_l = dfs(cur.left)
#             sums_r, f_r, left_r, right_r = 0, True, float('inf'), cur.val
#             if cur.right:
#                 sums_r, f_r, left_r, right_r = dfs(cur.right)
#             if f_l and f_r and right_l < cur.val < left_r:
#                 sums = sums_l+sums_r+cur.val
#                 res = max(res,sums)
#                 return sums, True, left_l, right_r
#             else:
#                 return 0, False, -float('inf'), float('inf')

#         if not root:
#             return 0
#         res = 0
#         dfs(root)
#         return res

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        res = 0
        def traverse(root):
            '''return status_of_bst, size_of_bst, left_bound, right_bound'''
            nonlocal res
            if not root: return 1, 0, None, None # this subtree is empty
            
            ls, l, ll, lr = traverse(root.left)
            rs, r, rl, rr = traverse(root.right)
            
            if ((ls == 2 and lr < root.val) or ls == 1) and ((rs == 2 and rl > root.val) or rs == 1):
		        # this subtree is a BST
                size = root.val + l + r
                res = max(res, size)
                return 2, size, (ll if ll is not None else root.val), (rr if rr is not None else root.val)
            return 0, None, None, None # this subtree is not a BST
        
        traverse(root)
        return res