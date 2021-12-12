# class Solution:
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         n, m = len(grid), len(grid[0])
#         q = collections.deque()
#         visited = set()
#         q.append((0,0,k,0))
#         visited.add((0,0,k,0))
#         while q:
#             i,j,limit,step = q.popleft()
#             if (i,j) == (n-1,m-1):
#                 return step
#             for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#                 x, y = i+dx, j+dy
#                 if 0 <= x < n and 0 <= y < m:
#                     new_limit = limit-grid[x][y]
#                     if new_limit < 0 or (x,y,new_limit,step+1) in visited:
#                         continue
#                     q.append((x,y,new_limit,step+1))
#                     visited.add((x,y,new_limit,step+1))
#         return -1
    
# class Solution:
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         n, m = len(grid), len(grid[0])
#         q = collections.deque()
#         visited = set()
#         q.append((0,0,k,0))
#         visited.add((0,0,k))
#         while q:
#             i,j,limit,step = q.popleft()
#             if (i,j) == (n-1,m-1):
#                 return step
#             for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#                 x, y = i+dx, j+dy
#                 if 0 <= x < n and 0 <= y < m:
#                     new_limit = limit-grid[x][y]
#                     if new_limit < 0 or (x,y,new_limit) in visited:
#                         continue
#                     q.append((x,y,new_limit,step+1))
#                     visited.add((x,y,new_limit))
#         return -1

from collections import deque
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        s = [[[False]*(k+1) for j in range(m)] for i in range(n)]
        q = deque()
        def consider(x, y, z, d):
            if x<0 or x>=n or y<0 or y>=m: return
            z += grid[x][y]
            if z>k or s[x][y][z]: return
            s[x][y][z] = True
            q.append((x, y, z, d))
        consider(0, 0, 0, 0)
        while q:
            x, y, z, d = q.popleft()
            consider(x+1, y, z, d+1)
            consider(x-1, y, z, d+1)
            consider(x, y+1, z, d+1)
            consider(x, y-1, z, d+1)
            if x==n-1 and y==m-1: return d
        return -1


dij = [(-1,0),(1,0),(0,-1),(0,1)]
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        dist = [[float('inf')]*m for _ in range(n)]
        dist[0][0] = 0
        def bfs(q):
            heapq.heapify(q)
            while q:
                d, i, j = heapq.heappop(q)
                if d > dist[i][j]:
                    continue
                for di, dj in dij:
                    di += i  
                    dj += j  
                    if 0 <= di < n and 0 <= dj < m and grid[di][dj] == 0 and 1+d < dist[di][dj]:
                        dist[di][dj] = d+1
                        heapq.heappush(q,(d+1,di,dj))
            # print(dist)
            return

        bfs([(0,0,0)])
        for _ in range(k):
            q = []
            tmp = [[0]*m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    tmp[i][j] = dist[i][j]
                    for di, dj in dij:
                        di += i 
                        dj += j 
                        if 0 <= di < n and 0 <= dj < m and dist[di][dj]+1 < tmp[i][j]:
                            tmp[i][j] = dist[di][dj]+1
                            q.append((tmp[i][j],i,j))
            for i in range(n):
                for j in range(m):
                    dist[i][j] = tmp[i][j]
            bfs(q)
            
        res = dist[n-1][m-1]
        return res if res < float('inf') else -1



dij = [(-1,0),(1,0),(0,-1),(0,1)]
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        seen = set()
        seen.add((0,0,0))
        cur = [(0,0,0)]
        step = 0
        while cur:
            sz = len(cur)
            nxt = []
            for i, j, d in cur:
                if (i,j) == (n-1,m-1):
                    return step 
                for di, dj in dij:
                    di += i 
                    dj += j 
                    if 0 <= di < n and 0 <= dj < m:
                        delta = (grid[di][dj] == 1)
                        if (di,dj,d+delta) not in seen and d+delta <= k:
                            seen.add((di,dj,d+delta))
                            nxt.append((di,dj,d+delta))  
            step += 1
            cur = nxt          
        return -1


dij = [(-1,0),(1,0),(0,-1),(0,1)]
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        if k >= n+m-2:
            return n+m-2
        removes = [[float('inf')]*m for _ in range(n)]
        removes[0][0] = 0
        q = deque([(0,0,0,0)])
        while q:
            i, j, d, step = q.popleft()
            if (i,j) == (n-1,m-1):
                return step 
            for di, dj in dij:
                di += i 
                dj += j 
                if 0 <= di < n and 0 <= dj < m:
                    delta = (grid[di][dj] == 1)
                    if d+delta < removes[di][dj] and d+delta <= k:
                        removes[di][dj] = d+delta
                        q.append((di,dj,d+delta,step+1))   
        return -1


dij = [(-1,0),(1,0),(0,-1),(0,1)]
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        if k >= n+m-2:
            return n+m-2
        removes = defaultdict(lambda : float('inf'))
        removes[0,0] = 0
        q = deque([(0,0,0,0)])
        while q:
            i, j, d, step = q.popleft()
            if (i,j) == (n-1,m-1):
                return step 
            for di, dj in dij:
                di += i 
                dj += j 
                if 0 <= di < n and 0 <= dj < m:
                    delta = (grid[di][dj] == 1)
                    if d+delta < removes[di,dj] and d+delta <= k:
                        removes[di,dj] = d+delta
                        q.append((di,dj,d+delta,step+1))   
        return -1



