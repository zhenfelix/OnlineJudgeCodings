# class Solution:
#     def largestMagicSquare(self, grid: List[List[int]]) -> int:
#         res = 1
#         n, m = len(grid), len(grid[0])
#         horizon = [[0]*(m+1) for _ in range(n+1)]
#         vertical = [[0]*(m+1) for _ in range(n+1)]
#         for i in range(n):
#             for j in range(m):
#                 horizon[i][j] = horizon[i][j-1] + grid[i][j]
#                 vertical[i][j] = vertical[i-1][j] + grid[i][j]
#         # print(horizon)
#         # print(vertical)
#         for k in range(2, min(n,m)+1):
#             for i in range(n-k+1):
#                 for j in range(m-k+1):
#                     a = sum(grid[i+p][j+p] for p in range(k))
#                     b = sum(grid[i+k-1-p][j+p] for p in range(k))
#                     # if (i==1 and j==1 and k==2):
#                     #     print(a,b)
#                     if a != b:
#                         continue
#                     if any(horizon[i+p][j+k-1]-horizon[i+p][j-1] != a for p in range(k)):
#                         continue
#                     if any(vertical[i+k-1][j+p]-vertical[i-1][j+p] != a for p in range(k)):
#                         continue
#                     res = max(res,k)
#         return res


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        horizon = [[0]*(m+1) for _ in range(n+1)]
        vertical = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                horizon[i][j] = horizon[i][j-1] + grid[i][j]
                vertical[i][j] = vertical[i-1][j] + grid[i][j]
        # print(horizon)
        # print(vertical)
        for k in range(2, min(n,m)+1)[::-1]:
            for i in range(n-k+1):
                for j in range(m-k+1):
                    a = sum(grid[i+p][j+p] for p in range(k))
                    b = sum(grid[i+k-1-p][j+p] for p in range(k))
                    # if (i==1 and j==1 and k==2):
                    #     print(a,b)
                    if a != b:
                        continue
                    if any(horizon[i+p][j+k-1]-horizon[i+p][j-1] != a for p in range(k)):
                        continue
                    if any(vertical[i+k-1][j+p]-vertical[i-1][j+p] != a for p in range(k)):
                        continue
                    return k
        return 1



