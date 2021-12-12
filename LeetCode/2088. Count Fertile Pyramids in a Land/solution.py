class Solution:
    def calc(self, grid):
        n, m = len(grid), len(grid[0])
        left = [[0]*m for _ in range(n)]
        right = [[0]*m for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and j:
                    left[i][j] = left[i][j-1]+grid[i][j-1]
            for j in range(m)[::-1]:
                if grid[i][j] == 1 and j < m-1:
                    right[i][j] = right[i][j+1]+grid[i][j+1]
        for j in range(m):
            ii = 0
            for i in range(n):
                while ii < n and min(left[ii][j],right[ii][j]) >= ii-i:
                    ii += 1
                cnt += ii-i-1 if grid[i][j] == 1 else 0
                # print(i,j,cnt)
            ii = n-1
            for i in range(n)[::-1]:
                while ii >= 0 and min(left[ii][j],right[ii][j]) >= i-ii:
                    ii -= 1
                cnt += i-ii-1 if grid[i][j] == 1 else 0
                # print(i,j,cnt)
        return cnt 
    def countPyramids(self, grid: List[List[int]]) -> int:
        return self.calc(grid)