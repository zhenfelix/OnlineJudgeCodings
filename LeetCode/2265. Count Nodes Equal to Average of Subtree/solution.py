# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(cur):
            nonlocal ans
            if not cur:
                return 0, 0
            left_sum, left_cnt = dfs(cur.left)
            right_sum, right_cnt = dfs(cur.right)
            sums = left_sum+right_sum+cur.val
            cnt = left_cnt+right_cnt+1
            if sums//cnt == cur.val:
                ans += 1
            return sums, cnt 
        dfs(root)
        return ans 