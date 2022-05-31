class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fires = [(r,c) for r in range(n) for c in range(m) if grid[r][c] == 1]
        drc = [-1,0,1,0,-1]
        def bfs(t):
            q = [(r,c,True) for r, c in fires]
            visited = set(fires)
            path = set()
            cnt = 0
            occupy = False
            while q or cnt <= t:
                # print(t,cnt,q,visited)
                nq = []
                if cnt == t and (0,0) not in visited:
                    q.append((0,0,False))
                    path.add((0,0))
                for r,c,flag in q:
                    # if r == n-1 and c == m-1:
                        # if flag:
                        #     return False
                        # else:
                        # if not flag:
                        #     return True
                    for dr, dc in zip(drc[1:],drc[:-1]):
                        dr += r  
                        dc += c                          
                        if 0 <= dr < n and 0 <= dc < m:
                            if grid[dr][dc] == 2:
                                continue
                            if flag:
                                if (dr,dc) not in visited:
                                    nq.append((dr,dc,True))
                                    visited.add((dr,dc))
                            else:
                                if (dr,dc) == (n-1,m-1) and not occupy:
                                    return True
                                if (dr,dc) not in visited and (dr,dc) not in path:
                                    nq.append((dr,dc,False))
                                    path.add((dr,dc))
                if (n-1,m-1) in visited:
                    occupy = True
                q = nq
                cnt += 1
            return False

        lo, hi = 0, n*m+1
        while lo <= hi:
            mid = (lo+hi)//2
            # print(mid,bfs(mid))
            if bfs(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        if hi < 0:
            return -1
        if hi > n*m:
            return 10**9
        return hi






class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        drc = [-1,0,1,0,-1]
        def getnext(r,c,delta,dist):
            for dr, dc in zip(drc[1:],drc[:-1]):
                dr += r 
                dc += c  
                if (dr,dc) == (n-1,m-1) and dist[r][c]+1+delta == dist[dr][dc]:
                    yield dr, dc 
                if 0 <= dr < n and 0 <= dc < m and dist[r][c]+1+delta < dist[dr][dc]:
                    dist[dr][dc] = dist[r][c] + 1
                    yield dr, dc 
            return

        def bfs(q,delta,dist,judge):
            while q:
                r, c = q.popleft()
                if judge and (r,c) == (n-1,m-1):
                    return True
                for nr, nc in getnext(r,c,delta,dist):
                    q.append((nr,nc))
            return False

        dist_fire = [[float('inf')]*m for _ in range(n)]
        q_fire = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    dist_fire[i][j] = 0
                elif grid[i][j] == 1:
                    q_fire.append((i,j))
                    dist_fire[i][j] = 0
        bfs(q_fire,0,dist_fire,False)
        # print(dist_fire)

        lo, hi = 0, 10**9
        while lo <= hi:
            mid = (lo+hi)//2
            q_ = deque([(0,0)])
            dist_ = [[0]*m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    dist_[i][j] = dist_fire[i][j]
            dist_[0][0] = 0
            if bfs(q_,mid,dist_,True):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi 



