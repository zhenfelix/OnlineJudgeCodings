class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        hq = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q.append((i,j))
                    hq.append((0,i,j))
                else:
                    grid[i][j] = inf 
        drc = [-1,0,1,0,-1]

        while q:
            r, c = q.popleft()
            for dr, dc in zip(drc[1:],drc[:-1]):
                dr += r 
                dc += c 
                if 0 <= dr < n and 0 <= dc < m and grid[dr][dc] == inf:
                    grid[dr][dc] = grid[r][c]+1
                    q.append((dr,dc))
                    hq.append((grid[dr][dc],dr,dc))
        tot = n*m  
        parent = [i for i in range(tot)]
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def connect(u,v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv 
            return
        for d, i, j in sorted(hq, reverse = True):
            u = i*m+j
            for di, dj in zip(drc[:-1],drc[1:]):
                di += i  
                dj += j  
                if 0 <= di < n and 0 <= dj < m and grid[di][dj] >= d:
                    v = di*m+dj 
                    connect(u,v)
            if find(0) == find(tot-1):
                return d 
        return -1