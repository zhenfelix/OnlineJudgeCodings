class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])
        grid = [row+[0] for row in grid2]
        grid += [[0]*(m+1)]
        dxy = [-1,0,1,0,-1]

        def dfs(x, y):
            flag = (grid1[x][y] == 1)
            grid[x][y] = -1
            for dx, dy in zip(dxy,dxy[1:]):
                dx += x 
                dy += y 
                if grid[dx][dy] == 1:
                    flag &= dfs(dx,dy)
            return flag

        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += dfs(i,j)
        return cnt


class Solution:
    def countSubIslands(self, B, A):
        n, m = len(A), len(A[0])

        def dfs(i, j):
            if not (0 <= i < n and 0 <= j < m and A[i][j] == 1): return 1
            A[i][j] = 0
            res = B[i][j]
            for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                res &= dfs(i + di, j + dj)
            return res
            
        return sum(dfs(i, j) for i in range(n) for j in range(m) if A[i][j])        