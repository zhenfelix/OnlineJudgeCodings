class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        ans = [0]*m 
        for j in range(m):
            for i in range(n):
                ans[j] = max(ans[j],len(str(grid[i][j])))
        return ans 