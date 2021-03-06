# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def dfs(i,j,p,q):
            if i > j:
                return None
            root = TreeNode(preorder[i])
            idx = mp[preorder[i]]
            root.left = dfs(i+1,i+idx-p,p,idx-1)
            root.right = dfs(i+idx-p+1,j,idx+1,q)
            return root
        mp = {v: i for i,v in enumerate(inorder)}
        n = len(preorder)
        return dfs(0,n-1,0,n-1)