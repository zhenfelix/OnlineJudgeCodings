class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def calc(r, c):
            s = 0
            for x in range(r, r+3):
                for y in range(c, c+3):
                    s += grid[x][y]
            s -= (grid[r+1][c]+grid[r+1][c+2])
            return s 
        ans = 0
        for i in range(n-2):
            for j in range(m-2):
                ans = max(ans, calc(i,j))
        return ans 