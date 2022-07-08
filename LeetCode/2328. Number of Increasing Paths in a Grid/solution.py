class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        drc = [-1,0,1,0,-1]
        n, m = len(grid), len(grid[0])

        @cache
        def dfs(r,c):
            ans = 1
            for dr, dc in zip(drc[1:],drc[:-1]):
                dr += r  
                dc += c  
                if 0 <= dr < n and 0 <= dc < m and grid[dr][dc] < grid[r][c]:
                    ans += dfs(dr,dc)
            return ans%MOD

        res = 0
        for i in range(n):
            for j in range(m):
                res += dfs(i,j)
                res %= MOD
        return res

        



class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        drc = [-1,0,1,0,-1]
        n, m = len(grid), len(grid[0])
        dp = [[1]*m for _ in range(n)]
        arr = []
        g = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(n):
            for j in range(m):
                arr.append((grid[i][j],i,j))
                for dr, dc in zip(drc[1:],drc[:-1]):
                    dr += i 
                    dc += j  
                    if 0 <= dr < n and 0 <= dc < m and grid[dr][dc] > grid[i][j]:
                        g[i,j].append((dr,dc))
                        indegree[dr,dc] += 1
        mi = min(arr)[0]
        q = deque()
        for i in range(n):
            for j in range(m):
                if indegree[i,j] == 0:
                    q.append((i,j))
        ans = 0
        while q:
            r, c = q.popleft()
            ans += dp[r][c]
            ans %= MOD
            for nr, nc in g[r,c]:
                dp[nr][nc] += dp[r][c]
                dp[nr][nc] %= MOD
                indegree[nr,nc] -= 1 
                if indegree[nr,nc] == 0:
                    q.append((nr,nc))
        return ans 


        
