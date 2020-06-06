# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:

#     def BSTSequences(self, root: TreeNode) -> List[List[int]]:
#         def dfs(i,j,path):
#             if i == n or j == m:
#                 path += arr1[i:]
#                 path += arr2[j:]
#                 res.append(path[:])
#                 return
#             dfs(i+1,j,path+[arr1[i]])
#             dfs(i,j+1,path+[arr2[j]])
#             return

#         if not root: return [[]]
#         arrs1 = self.BSTSequences(root.left)
#         arrs2 = self.BSTSequences(root.right)
#         ans = []
#         for arr1 in arrs1:
#             for arr2 in arrs2:
#                 res = []
#                 n, m = len(arr1), len(arr2)
#                 dfs(0,0,[root.val])
#                 ans += res
#         return ans

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        res = []
        def topo(q, path):
            if not q:
                res.append(path)
                return
            for i, cur in enumerate(q):
                tmp = []
                if cur.left:
                    tmp.append(cur.left)
                if cur.right:
                    tmp.append(cur.right)
                topo(q[:i]+q[i+1:]+tmp,path+[cur.val])
            return

        topo([root], [])
        return res

