# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def minCameraCover(self, root: TreeNode) -> int:
#         def dfs(cur):
#             res = [float('inf')]*4
#             if not cur:
#                 res[1] = 0
#                 return res
#             l = dfs(cur.left)
#             r = dfs(cur.right)
#             for i in range(4):
#                 if i == 2:
#                     continue
#                 for j in range(4):
#                     if j == 2:
#                         continue
#                     oleft, oright = i//2, j//2
#                     for occupy in range(2):
#                         if occupy == 0 and (i == 0 or j == 0):
#                             continue
#                         valid = oleft|oright|occupy
#                         k = 2*occupy+valid
#                         res[k] = min(res[k], l[i]+r[j]+occupy)
#             # print(cur,res)
#             return res

#         ans = dfs(root)
#         return min(ans[1],ans[3])


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> List[int]:
            if not root:
                return [float("inf"), 0, 0]
            
            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)
            a = lc + rc + 1
            b = min(a, la + rb, ra + lb)
            c = min(a, lb + rb)
            return [a, b, c]
        
        a, b, c = dfs(root)
        return b


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/binary-tree-cameras/solution/jian-kong-er-cha-shu-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。