# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
    #     ans = [None]
    #     max_ans = [-1]
    #     def dfs(node, depth):
    #         if not node:
    #             return depth
    #         # print(node.val, depth)
    #         left = dfs(node.left, depth+1)
    #         right = dfs(node.right, depth+1)
    #         # print(node.val, left, right)
    #         if left == right and left >= max_ans[0]:
    #             ans[0] = node
    #             max_ans[0] = left
    #             # print(ans[0].val)
    #         max_depth = max(left, right)
    #         # print(node.val, max_depth)
    #         return max_depth
    #     dfs(root, 0)
    #     return ans[0]
    

    def lcaDeepestLeaves(self, root):
        def helper(root):
            if not root:
                return 0, None
            d1, lca1 = helper(root.left)
            d2, lca2 = helper(root.right)
            if d1 > d2:
                node = lca1
            elif d1 < d2:
                node = lca2
            else:
                node = root
            return max(d1, d2) + 1, node
        return helper(root)[1]