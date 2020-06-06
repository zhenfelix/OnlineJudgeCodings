from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(i,j,k):
            if i < 0 or i >= m or j < 0 or j >= m or k >= n:
                return 0
            if i == j:
                res = grid[k][j] 
            else:
                res = grid[k][i] + grid[k][j]
            res += max(dfs(min(i+di,j+dj),max(i+di,j+dj),k+1) for di in range(-1,2) for dj in range(-1,2))
            return res
        return dfs(0,m-1,0)
