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








from heapq import *


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        INF = 2000000000
        burn = [[INF] * M for _ in range(N)]
        q = []
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c == 1:
                    burn[i][j] = -1
                    q.append((i, j, -1))
                elif c == 2:
                    burn[i][j] = -2
        f = 0
        while f < len(q):
            i, j, d = q[f]
            f += 1
            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                if 0 <= i + dx < N and 0 <= j + dy < M and burn[i + dx][j + dy] > d + 1:
                    q.append((i + dx, j + dy, d + 1))
                    burn[i + dx][j + dy] = d + 1
        cap = [[-1] * M for _ in range(N)]
        cap[0][0] = burn[0][0]
        # for any position (i,j) except (n-1,m-1)
        # cap[i][j]+t <= burn[i][j]
        heap = [(-burn[0][0], 0, 0, 0)]
        while heap:
            c, t, i, j = heappop(heap)
            c = -c
            if i == N - 1 and j == M - 1:
                return max(min(c, 1000000000), -1)
            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                if 0 <= i + dx < N and 0 <= j + dy < M:
                    if i + dx == N - 1 and j + dy == M - 1:
                        c2 = min(c, burn[i + dx][j + dy] - t)
                    else:
                        c2 = burn[i + dx][j + dy] - t - 1
                    if c2 > cap[i + dx][j + dy]:
                        cap[i + dx][j + dy] = c2
                        heappush(heap, (-c2, t + 1, i + dx, j + dy))
        else:
            return -1



作者：ling-jian-2012
链接：https://leetcode.cn/problems/escape-the-spreading-fire/solution/bfs-prim-by-ling-jian-2012-67ov/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。











from heapq import *


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        INF = 2000000000
        burn = [[INF] * M for _ in range(N)]
        q = []
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c == 1:
                    burn[i][j] = -1
                    q.append((i, j, -1))
                elif c == 2:
                    burn[i][j] = -2
        f = 0
        while f < len(q):
            i, j, d = q[f]
            f += 1
            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                if 0 <= i + dx < N and 0 <= j + dy < M and burn[i + dx][j + dy] > d + 1:
                    q.append((i + dx, j + dy, d + 1))
                    burn[i + dx][j + dy] = d + 1
        cap = [[-1] * M for _ in range(N)]
        cap[0][0] = burn[0][0]
        q0 = [(0, 0)]
        q1 = []
        q2 = []
        current = burn[0][0]
        while q0 or q1 or q2:
            while q0:
                i, j = q0.pop()
                if i == N - 1 and j == M - 1:
                    return max(min(current, 1000000000), -1)
                if cap[i][j] > current:
                    continue
                for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    if 0 <= i + dx < N and 0 <= j + dy < M and grid[i + dx][j + dy] == 0:
                        if burn[i + dx][j + dy] == burn[i][j] + 1:
                            dc = 0
                        else:
                            if burn[i + dx][j + dy] == burn[i][j]:
                                dc = 1
                            else:
                                dc = 2
                            if i + dx == N - 1 and j + dy == M - 1:
                                dc -= 1
                        if cap[i + dx][j + dy] < current - dc:
                            cap[i + dx][j + dy] = current - dc
                            (q0, q1, q2)[dc].append((i + dx, j + dy))
            q0, q1, q2 = q1, q2, q0
            current -= 1
        else:
            return -1


作者：ling-jian-2012
链接：https://leetcode.cn/problems/escape-the-spreading-fire/solution/bfs-prim-by-ling-jian-2012-67ov/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。