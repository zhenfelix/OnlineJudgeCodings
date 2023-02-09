class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(grid), len(grid[0])
        parent = list(range(n*m+1))
        sz = [1]*(n*m+1)
        sz[-1] = 0 
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def connect(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
                sz[rv] += sz[ru]
            return
        edge = [(grid[0][0],0,n*m)]
        def calc(i,j):
            return i*m+j
        for i in range(n):
            for j in range(m):
                if i: edge.append((max(grid[i][j],grid[i-1][j]),calc(i,j),calc(i-1,j)))
                if j: edge.append((max(grid[i][j],grid[i][j-1]),calc(i,j),calc(i,j-1)))
        edge.sort()
        cnt, mx = [0], [0]
        for val, u, v in edge:
            connect(u,v)
            cnt.append(sz[find(n*m)])
            mx.append(val)
        # print(cnt,mx)
        ans = []
        for q in queries:
            ans.append(cnt[bisect_right(mx,q-1)-1])

        return ans


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(grid), len(grid[0])
        dxy = [-1,0,1,0,-1]
        arr, mx = [0], [0]
        hq = [(grid[0][0],0,0)]
        grid[0][0] = 0
        while hq:
            v, i, j = heappop(hq)
            if v > mx[-1]:
                mx.append(v)
                arr.append(arr[-1])
            arr[-1] += 1
            for dx, dy in zip(dxy[1:],dxy[:-1]):
                dx += i 
                dy += j 
                if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] > 0:
                    heappush(hq, (grid[dx][dy],dx,dy))
                    grid[dx][dy] = 0
        # print(arr)
        # print(mx)
        ans = []
        for q in queries:
            i = bisect.bisect_right(mx, q-1)-1
            # print(i)
            ans.append(arr[i])
        return ans
