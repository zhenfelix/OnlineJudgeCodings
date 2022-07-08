class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        dist = [[float('inf')]*m for _ in range(n)]
        q.append((0,0,0))
        dist[0][0] = 0
        drc = [-1,0,1,0,-1]
        while q:
            r, c, d = q.popleft()
            if d > dist[r][c]:
                continue
            # print(r,c,d)
            # print(dist)
            if (r,c) == (n-1,m-1):
                return dist[r][c]
            for dr, dc in zip(drc[1:],drc[:-1]):
                dr += r 
                dc += c 
                if 0 <= dr < n and 0 <= dc < m and d+grid[dr][dc] < dist[dr][dc]:
                    dist[dr][dc] = d+grid[dr][dc]
                    if grid[dr][dc] == 0:
                        q.appendleft((dr,dc,dist[dr][dc]))
                    else:
                        q.append((dr,dc,dist[dr][dc]))
        return -1

