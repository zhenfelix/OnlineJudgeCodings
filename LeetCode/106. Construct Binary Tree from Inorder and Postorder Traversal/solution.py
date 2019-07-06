# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
#         mp = {}
#         n = len(inorder)
#         for idx, val in enumerate(inorder):
#             mp[val] = idx
#         def helper(left, right, lo, hi):
#             if left <= right:
#                 node = TreeNode(postorder[hi])
#                 mid = mp[node.val]
#                 # for i in range(left, right+1):
#                 #     if node.val == inorder[i]:
#                 #         mid = i
#                 #         break
#                 node.left = helper(left, mid-1, lo, lo+mid-1-left)
#                 node.right = helper(mid+1, right, lo+mid-1-left+1, hi-1)
#                 return node
#             return None
#         return helper(0,n-1,0,n-1)


# Don't use top voted Python solution for interview, here is why.

class Solution:
    def buildTree(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        def recur(low, high):
            if low > high: return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inorder)-1)
                