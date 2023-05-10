class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        dxy = [-1,0,1,0,-1]
        def bfs(i,j):
            # print(i,j)
            cnt = grid[i][j]
            grid[i][j] = 0
            q = deque()
            q.append((i,j))
            while q:
                x, y = q.popleft()
                # print(x,y)
                for dx, dy in zip(dxy[1:],dxy[:-1]):
                    dx += x 
                    dy += y 
                    if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] > 0:
                        cnt += grid[dx][dy]
                        grid[dx][dy] = 0 
                        q.append((dx,dy))
            return cnt
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ans = max(ans, bfs(i,j))
        return ans