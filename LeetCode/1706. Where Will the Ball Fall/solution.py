class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        ans = [-1]*m
        for c in range(m):
            cur = c 
            r = 0
            while r < n:
                if grid[r][cur] == 1:
                    if cur < m-1 and grid[r][cur+1] == 1:
                        cur += 1
                    else:
                        break
                else:
                    if cur > 0 and grid[r][cur-1] == -1:
                        cur -= 1
                    else:
                        break
                r += 1
            if r == n:
                ans[c] = cur

        return ans