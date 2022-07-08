class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [grid[0][j] for j in range(m)]
        for i in range(n-1):
            ndp = [float('inf')]*m 
            for j in range(m):
                v = grid[i][j]
                for k in range(m):
                    ndp[k] = min(ndp[k], dp[j]+moveCost[v][k])
            dp = [grid[i+1][j]+ndp[j] for j in range(m)]
            # print(dp)
        return min(dp)