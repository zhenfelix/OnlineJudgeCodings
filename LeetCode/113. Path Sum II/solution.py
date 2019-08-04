# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node, target, path, ans):
            if not node:
                return
        
            if node.val == target and not node.left and not node.right:
                # print([path+[node.val]])
                ans += [path+[node.val]]
                
            dfs(node.left, target-node.val, path+[node.val], ans)
            dfs(node.right, target-node.val, path+[node.val], ans)
            return
        
        ans_ = []
        dfs(root, sum, [], ans_)
        return ans_