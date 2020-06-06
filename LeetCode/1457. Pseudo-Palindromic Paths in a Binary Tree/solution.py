# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root):

        def dfs(root, count=0):
            if not root: return 0
            count ^= 1 << (root.val - 1)
            res = dfs(root.left, count) + dfs(root.right, count)
            if root.left == root.right:
                if count & (count - 1) == 0:
                    res += 1
            count ^= 1 << (root.val - 1)
            return res
        return dfs(root)

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def pseudoPalindromicPaths (self, root: TreeNode) -> int:
#         res = 0
#         def dfs(cur,cnt):
#             nonlocal res
#             # print(cnt,cur)
#             if not cur:
#                 return

#             cnt[cur.val] += 1
#             if not cur.left and not cur.right:
#                 if sum(x&1 for x in cnt.values()) <= 1:
#                     res += 1
#                 # return
            
#             dfs(cur.left,cnt)
#             dfs(cur.right,cnt)
#             cnt[cur.val] -= 1
#             return

#         dfs(root,Counter())
#         return res