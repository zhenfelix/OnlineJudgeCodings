# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = []
        def midOrder(cur):
            if cur:
                midOrder(cur.left)
                res.append(cur.val)
                midOrder(cur.right)
                
        def dfs(left,right):
            if left <= right:
                mid = (left+right)//2
                cur = TreeNode(res[mid])
                cur.left = dfs(left,mid-1)
                cur.right = dfs(mid+1,right)
                return cur
            return None
        
        midOrder(root)
        # print(res)
        return dfs(0,len(res)-1)