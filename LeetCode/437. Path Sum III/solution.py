# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node, pathsum, prefixsum):
            if not node:
                return 0
            ans = 0
            pathsum += node.val
            if pathsum-sum in prefixsum:
                ans += prefixsum[pathsum-sum]
            if pathsum in prefixsum:
                prefixsum[pathsum] += 1
            else:
                prefixsum[pathsum] = 1
            ans += dfs(node.left, pathsum, prefixsum)
            ans += dfs(node.right, pathsum, prefixsum)
            prefixsum[pathsum] -= 1
            return ans
        return dfs(root,0,{0:1})
            