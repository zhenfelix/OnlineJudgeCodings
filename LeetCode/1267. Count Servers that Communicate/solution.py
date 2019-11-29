class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rows = [0]*n
        cols = [0]*m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    res += 1
        return res
