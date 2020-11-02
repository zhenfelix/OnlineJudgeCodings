class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        total, x, y = 0, -1, -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    total += 1
        res = [0]
        def dfs(i,j,cnt):
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                di += i 
                dj += j
                if 0 <= di < n and 0 <= dj < m and grid[di][dj] in [0,2]:
                    if grid[di][dj] == 2:
                        if cnt == total:
                            res[0] += 1
                    else:
                        grid[di][dj] = -1
                        dfs(di,dj,cnt+1)
                        grid[di][dj] = 0
            return 
        dfs(x,y,0)
        return res[-1]
