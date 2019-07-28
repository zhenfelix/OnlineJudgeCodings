class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        ans = 0
        n, m =len(grid), len(grid[0])
        dp_row, dp_col= [[0]*m for _ in range(n)], [[0]*m for _ in range(n)]
        for j in range(m):
            for i in range(n):
                if grid[i][j] == 1:
                    if j > 0:
                        dp_col[i][j] = dp_col[i][j-1]+1
                    else:
                        dp_col[i][j] = 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i > 0:
                        dp_row[i][j] = dp_row[i-1][j]+1
                    else:
                        dp_row[i][j] = 1
                    
                    d = ans+1
                    while d <= dp_col[i][j]:
                        if dp_row[i][j] >= d and dp_row[i][j-d+1] >= d and dp_col[i-d+1][j] >= d:
                            ans = d
                        d += 1
        return ans*ans
        