class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cc = Counter()
        n = len(grid)
        ans = 0 
        for i in range(n):
            cc[tuple([grid[i][j] for j in range(n)])] += 1
        for j in range(n):
            ans += cc[tuple([grid[i][j] for i in range(n)])]
        return ans 