class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        left, right = 0, sum(grid[0])
        res = float('inf')
        for i in range(n):
            right -= grid[0][i]
            if i:
                left += grid[1][i-1]
            res = min(res, max(left,right))
        return res