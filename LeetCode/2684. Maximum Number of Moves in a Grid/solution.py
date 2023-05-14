class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(r,c):
            res = 0
            if c+1 < m:
                if r-1 >= 0 and grid[r-1][c+1] > grid[r][c]:
                    res = max(res,dfs(r-1,c+1)+1)
                if r+1 < n and grid[r+1][c+1] > grid[r][c]:
                    res = max(res,dfs(r+1,c+1)+1)
                if grid[r][c+1] > grid[r][c]:
                    res = max(res,dfs(r,c+1)+1)
            return res 
        return max(dfs(i,0) for i in range(n))