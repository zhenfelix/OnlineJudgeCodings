class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rows = [[] for _ in range(n)]
        cols = [[] for _ in range(m)]
        rows[0] = [(0,0)]
        cols[0] = [(0,0)]
        dist = [[inf]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                while rows[i] and rows[i][0][1] < j:
                    heappop(rows[i])
                if rows[i]:
                    dist[i][j] = min(dist[i][j], rows[i][0][0]+1)
                while cols[j] and cols[j][0][1] < i:
                    heappop(cols[j])
                if cols[j]:
                    dist[i][j] = min(dist[i][j], cols[j][0][0]+1)
                v = grid[i][j]
                heappush(rows[i],(dist[i][j],j+v))
                heappush(cols[j],(dist[i][j],i+v))
        res = dist[-1][-1]
        return res if res < inf else -1


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rows = [[] for _ in range(n)]
        cols = [[] for _ in range(m)]
        dist = [[inf]*m for _ in range(n)]
        dist[-1][-1] = 1
        for i in range(n)[::-1]:
            for j in range(m)[::-1]:
                v = grid[i][j]
                if i < n-1:
                    idx = bisect_left(cols[j],-i-v)
                    if idx < len(cols[j]):
                        dist[i][j] = min(dist[i][j], dist[-cols[j][idx]][j]+1)
                if j < m-1:
                    idx = bisect_left(rows[i],-j-v)
                    if idx < len(rows[i]):
                        dist[i][j] = min(dist[i][j], dist[i][-rows[i][idx]]+1)
                while cols[j] and dist[-cols[j][-1]][j] >= dist[i][j]:
                    cols[j].pop()
                cols[j].append(-i)
                while rows[i] and dist[i][-rows[i][-1]] >= dist[i][j]:
                    rows[i].pop()
                rows[i].append(-j)
        res = dist[0][0]
        return res if res < inf else -1
        


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        def find(u,parent):
            if parent[u] != u:
                parent[u] = find(parent[u],parent)
            return parent[u]
        def connect(u,v,parent):
            ru, rv = find(u,parent), find(v,parent)
            if ru != rv:
                parent[ru] = rv
            return
        n, m = len(grid), len(grid[0])
        rows = [list(range(m)) for _ in range(n)]
        cols = [list(range(n)) for _ in range(m)]
        dist = [[inf]*m for _ in range(n)]
        dist[0][0] = 1
        q = deque()
        q.append((0,0))
        while q:
            i, j = q.popleft()
            v = grid[i][j]
            jmx = min(j+v,m-1)
            cur = j 
            while cur <= jmx:
                cur = find(cur,rows[i])
                cur += 1 
                if cur <= jmx and dist[i][cur] == inf:
                    q.append((i,cur))
                    dist[i][cur] = dist[i][j]+1
                    connect(j,cur,rows[i])
                    if cur+1 < m and dist[i][cur+1] < inf:
                        connect(j,cur+1,rows[i])
                    if i-1 >= 0 and dist[i-1][cur] < inf:
                        connect(i-1,i,cols[cur])
                    if i+1 < n and dist[i+1][cur] < inf:
                        connect(i,i+1,cols[cur])
            imx = min(i+v,n-1)
            cur = i 
            while cur <= imx:
                cur = find(cur,cols[j])
                cur += 1
                if cur <= imx and dist[cur][j] == inf:
                    q.append((cur,j))
                    dist[cur][j] = dist[i][j]+1
                    connect(i,cur,cols[j])
                    if cur+1 < n and dist[cur+1][j] < inf:
                        connect(i,cur+1,cols[j])
                    if j-1 >= 0 and dist[cur][j-1] < inf:
                        connect(j-1,j,rows[cur])
                    if j+1 < m and dist[cur][j+1] < inf:
                        connect(j,j+1,rows[cur])
        res = dist[-1][-1]
        return res if res < inf else -1