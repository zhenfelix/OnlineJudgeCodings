class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        n, m = len(grid), len(grid[0])
        horizon, vertical = [[0]*m for _ in range(n)], [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 'W':
                    if j > 0:
                        horizon[i][j] = horizon[i][j-1]
                    if grid[i][j] == 'E':
                        horizon[i][j] += 1
            for j in range(m-2,-1,-1):
                if grid[i][j] != 'W' and grid[i][j+1] != 'W':
                    horizon[i][j] = horizon[i][j+1]
        
        for j in range(m):
            for i in range(n):
                if grid[i][j] != 'W':
                    if i > 0:
                        vertical[i][j] = vertical[i-1][j]
                    if grid[i][j] == 'E':
                        vertical[i][j] += 1
            for i in range(n-2,-1,-1):
                if grid[i][j] != 'W' and grid[i+1][j] != 'W':
                    vertical[i][j] = vertical[i+1][j]
             
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    ans = max(ans, horizon[i][j]+vertical[i][j])
        
        return ans