class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cnt = [[[0,0] for _ in range(m)] for _ in range(n)]
        vertical = [[[0,0] for _ in range(m)] for _ in range(n)]
        horizontal = [[[0,0] for _ in range(m)] for _ in range(n)]
        mods = [2,5]
        for i in range(n):
            for j in range(m):
                for k in range(2):
                    while grid[i][j]%mods[k] == 0:
                        cnt[i][j][k] += 1
                        grid[i][j] //= mods[k]
                    vertical[i][j][k] = cnt[i][j][k]+vertical[i-1][j][k]
                    horizontal[i][j][k] = cnt[i][j][k]+horizontal[i][j-1][k]
        ans = 0
        for i in range(n):
            for j in range(m):
                candidates = [[0,0] for _ in range(4)]
                for k in range(2):
                    candidates[0][k] = vertical[i][j][k]-cnt[i][j][k]
                    candidates[1][k] = vertical[-1][j][k]-vertical[i][j][k]
                    candidates[2][k] = horizontal[i][j][k]-cnt[i][j][k]
                    candidates[3][k] = horizontal[i][-1][k]-horizontal[i][j][k]
                for (a1,b1), (a2,b2) in combinations(candidates,2):
                    ans = max(ans, min(a1+a2+cnt[i][j][0],b1+b2+cnt[i][j][1]))
        return ans


