class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        pre = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != pre:
                    ans += 1
                    pre = grid[i][j]
            if pre == 1:
                ans += 1
                pre = 0
        
        for j in range(m):
            for i in range(n):
                if grid[i][j] != pre:
                    ans += 1
                    pre = grid[i][j]
            if pre == 1:
                ans += 1
                pre = 0
                
        return ans