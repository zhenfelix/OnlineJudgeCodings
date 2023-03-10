# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(cur, d):
            if d > len(arr):
                arr.append(0)
            arr[d-1] += cur.val
            if cur.left: dfs(cur.left, d+1)
            if cur.right: dfs(cur.right, d+1)
            return 
        dfs(root,1) 
        arr.sort()
        if len(arr) < k:
            return -1
        return arr[-k]
