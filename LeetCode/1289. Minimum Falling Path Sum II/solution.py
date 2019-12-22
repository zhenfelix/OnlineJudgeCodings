# from functools import lru_cache

# class Solution:
#     def minFallingPathSum(self, arr: List[List[int]]) -> int:
#         n = len(arr)
#         dp = []
#         for i, a in enumerate(arr):
#             dp.append(sorted([(x,j) for j, x in enumerate(a)]))

            
#         @lru_cache(None)
#         def dfs(row, col):            
#             if row == n-1:
#                 return arr[row][col]
#             if row == n:
#                 return 0
#             res = float('inf')
#             for j in range(n):
#                 c = 0
#                 while dp[row+1][c][1] in [j,col]:
#                     c += 1
#                 res = min(res, arr[row][col]+dfs(row+2,j)+dp[row+1][c][0])
#             return res

#         ans = float("inf")
#         for i in range(n):
#             ans = min(ans, dfs(0,i))
#         return ans

class Solution:
    def minFallingPathSum(self, A):
        for i in range(1, len(A)):
            r = heapq.nsmallest(2, A[i - 1])
            for j in range(len(A[0])):
                A[i][j] += r[1] if A[i - 1][j] == r[0] else r[0]
        return min(A[-1])