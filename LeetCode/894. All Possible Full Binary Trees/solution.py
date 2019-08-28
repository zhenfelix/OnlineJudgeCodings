# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def allPossibleFBT(self, N: int) -> List[TreeNode]:
#         if N & 1 == 0:
#             return []
#         if N == 1:
#             return [TreeNode(0)]
#         ans = []
#         for i in range(1,N,2):
#             left = self.allPossibleFBT(i)
#             right = self.allPossibleFBT(N-1-i)
#             for l in left:
#                 for r in right:
#                     node = TreeNode(0)
#                     node.left, node.right = l, r
#                     ans.append(node)
#         return ans

class Solution(object):
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]
                    
            
        