class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dij = [-1,0,1,0,-1]
        for i in range(n):
            for j in range(m):
                if (i+j)&1 != grid[i][j]&1:
                    grid[i][j] += 1
        hq = [(0,0,0)]
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        visited = [[0]*m for _ in range(n)]
        while hq:
            t, i, j = heappop(hq)
            if (i,j) == (n-1,m-1):
                return t
            if visited[i][j]: continue
            visited[i][j] = 1
            # print(t,i,j)
            for di, dj in zip(dij[1:],dij[:-1]):
                di += i 
                dj += j 
                if 0 <= di < n and 0 <= dj < m:
                    nt = grid[di][dj]
                    if t < nt:
                        heappush(hq,(nt,di,dj))
                    else:
                        heappush(hq,(t+1,di,dj))
        return -1