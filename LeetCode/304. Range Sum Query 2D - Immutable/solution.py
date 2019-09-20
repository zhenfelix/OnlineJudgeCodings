# class NumMatrix:

#     def __init__(self, matrix: List[List[int]]):
#         dp = matrix.copy()
#         n = len(dp)
#         self.n = n
#         if n > 0:
#             m = len(dp[0])
#         else:
#             return
#         for i in range(n):
#             for j in range(m):
#                 if i-1 >= 0:
#                     dp[i][j] += dp[i-1][j]
#                 if j-1 >= 0:
#                     dp[i][j] += dp[i][j-1]
#                 if i-1 >= 0 and j-1 >= 0:
#                     dp[i][j] -= dp[i-1][j-1]
#         self.dp = dp
#         return

#     def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
#         if self.n == 0:
#             return 0
#         sums = self.dp[row2][col2]
#         if row1-1 >= 0:
#             sums -= self.dp[row1-1][col2]
#         if col1-1 >= 0:
#             sums -= self.dp[row2][col1-1]
#         if row1-1 >= 0 and col1-1 >= 0:
#             sums += self.dp[row1-1][col1-1]
#         return sums

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix: return
        n, m = len(matrix), len(matrix[0])
        # self.n = n
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        self.dp = dp
        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        sums = self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]
        
        return sums


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)