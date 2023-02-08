class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        dist = [[inf]*m for _ in range(n)]
        dist[0][0] = 0
        q = [(0,0,0)]
        heapify(q)
        dxy = [-1,0,1,0,-1]
        while q:
            h, i, j = heappop(q)
            if h > dist[i][j]:
                continue
            if (i,j) == (n-1,m-1):
                return h 
            for di, dj in zip(dxy[1:],dxy[:-1]):
                di += i 
                dj += j 
                
                if 0 <= di < n and 0 <= dj < m:
                    nh = max(h,abs(heights[di][dj]-heights[i][j]))
                    if nh < dist[di][dj]:
                        heappush(q,(nh,di,dj))
                        dist[di][dj] = nh
        return -1

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q = [(0,0,0)]
        n, m = len(heights), len(heights[0])
        dp = [[float('inf')]*m for _ in range(n)]
        dp[0][0] = 0
        while q:
            cost, i, j = heapq.heappop(q)
            # if (i,j) == (n-1,m-1):
            #     return cost
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                di += i
                dj += j
                if 0 <= di < n and 0 <= dj < m:
                    ncost = max(cost, abs(heights[di][dj]-heights[i][j]))
                    if ncost < dp[di][dj]:
                        heapq.heappush(q,(ncost,di,dj))
                        dp[di][dj] = ncost
        return dp[-1][-1]


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        left, right = 0, 10**6
        while left <= right:
            mid = (left+right)//2
            q = deque([(0,0)])
            visited = set([(0,0)])
            while q:
                i, j = q.popleft()
                if (i,j) == (n-1,m-1):
                    break
                for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    di += i 
                    dj += j
                    if 0 <= di < n and 0 <= dj < m and (di,dj) not in visited and abs(heights[di][dj]-heights[i][j]) <= mid:
                        q.append((di,dj))
                        visited.add((di,dj))
            if (n-1,m-1) in visited:
                right = mid - 1
            else:
                left = mid + 1
        return left



class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        edges = []
        parent = [i*m+j for i in range(n) for j in range(m)]
        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
            return 
            
        for i in range(n):
            for j in range(m):
                if i:
                    edges.append((abs(heights[i][j]-heights[i-1][j]),i*m+j,(i-1)*m+j))
                if j:
                    edges.append((abs(heights[i][j]-heights[i][j-1]),i*m+j,i*m+(j-1)))
        for w, a, b in sorted(edges):
            union(a,b)
            if find(0) == find(n*m-1):
                return w 
        return 0
