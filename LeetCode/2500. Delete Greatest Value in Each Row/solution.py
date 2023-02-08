class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            grid[i] = sorted(grid[i])
        for j in range(m):
            ans += max(grid[i][j] for i in range(n))
        return ans 

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        for _ in range(m):
            tmp = 0
            for i in range(n):
                mx = max(grid[i])
                tmp = max(tmp, mx)
                for j in range(m):
                    if grid[i][j] == mx:
                        grid[i][j] = 0
                        break
            ans += tmp 
        return ans 