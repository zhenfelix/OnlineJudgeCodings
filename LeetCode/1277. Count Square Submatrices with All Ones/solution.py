# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         n, m = len(matrix), len(matrix[0])
#         dp = [[0]*m for _ in range(n)]
#         cnt = 0
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     dp[i][j] = 0
#                 else:
#                     if i == 0 or j == 0:
#                         dp[i][j] = 1
#                     else:
#                         width = dp[i][j-1]
#                         height = dp[i-1][j]
#                         sz = min(width,height)
#                         dp[i][j] = sz
#                         if matrix[i-sz][j-sz] == 1:
#                             dp[i][j] += 1
#                 cnt += dp[i][j]
#         print(dp)
#         return cnt


# - [DP with figure explanation](https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441620/DP-with-figure-explanation)
class Solution:
    def countSquares(self, A):
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                if A[i][j]:
                    A[i][j] = min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1])
        return sum(map(sum, A))