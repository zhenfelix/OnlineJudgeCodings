# https://leetcode.cn/contest/ubiquant2022/ranking/

class Solution:
    def lakeCount(self, field: List[str]) -> int:
        n, m = len(field), len(field[0])
        grid = []
        for i in range(n):
            grid.append(list(field[i]))
        def bfs(i,j):
            if grid[i][j] == '.':
                return 0
            q = deque()
            q.append((i,j))
            grid[i][j] = '.'
            while q:
                i,j = q.popleft()
                for dx in range(-1,2):
                    ni = i+dx
                    for dy in range(-1,2):
                        nj = j+dy
                        if dx == 0 and dy == 0:
                            continue
                        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 'W':
                            grid[ni][nj] = '.'
                            q.append((ni,nj))
            return 1

        ans = 0
        for x in range(n):
            for y in range(m):
                ans += bfs(x,y)
        return ans

