class Solution:
    def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:
        n = len(positions)
        positions.append([kx,ky])
        nmax = 50
        def bfs(sx,sy):
            dist = [[inf]*nmax for _ in range(nmax)]
            dist[sx][sy] = 0 
            q = deque()
            q.append((sx,sy))
            while q:
                x, y = q.popleft()
                for dx, dy in [(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]:
                    dx += x 
                    dy += y  
                    if 0 <= dx < nmax and 0 <= dy < nmax and dist[dx][dy] == inf:
                        dist[dx][dy] = dist[x][y]+1
                        q.append((dx,dy))
            return dist
        mat = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            x, y = positions[i]
            dist = bfs(x,y)
            # print(dist)
            for j in range(i+1,n+1):
                xx, yy = positions[j]
                mat[i][j] = mat[j][i] = dist[xx][yy]
        
        # print(mat)
        @lru_cache(None)
        def dfs(i,s,flag):
            if s == 0: return 0  
            candidates = [mat[i][j]+dfs(j,s^(1<<j),1-flag) for j in range(n) if (s>>j)&1]
            if flag: return max(candidates)
            return min(candidates)
        return dfs(n,(1<<n)-1,1)

