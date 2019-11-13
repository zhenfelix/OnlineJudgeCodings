class Solution:
    # def surfaceArea(self, grid: List[List[int]]) -> int:
#         res = 0
#         n , m = len(grid), len(grid[0])
#         for r in range(n):
#             for c in range(m):
#                 res += max(0, grid[r][c]-grid[r][c-1] if c > 0 else grid[r][c])
#             for c in range(m)[::-1]:
#                 res += max(0, grid[r][c]-grid[r][c+1] if c < m-1 else grid[r][c])
            
#         for c in range(m):
#             for r in range(n):
#                 res += max(0, grid[r][c]-grid[r-1][c] if r > 0 else grid[r][c])
#             for r in range(n)[::-1]:
#                 res += max(0, grid[r][c]-grid[r+1][c] if r < n-1 else grid[r][c])

#         for r in range(n):
#             for c in range(m):
#                 if grid[r][c] > 0:
#                     res += 2
                
#         return res

    def surfaceArea(self, grid):
        n, res = len(grid), 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]: res += 2 + grid[i][j] * 4
                if i: res -= min(grid[i][j], grid[i - 1][j]) * 2
                if j: res -= min(grid[i][j], grid[i][j - 1]) * 2
        return res