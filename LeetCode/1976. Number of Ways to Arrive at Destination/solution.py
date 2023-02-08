class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g =defaultdict(list)
        for u, v, t in roads:
            g[u].append((v,t))
            g[v].append((u,t))
        cnt = [0]*n 
        dist = [inf]*n 
        cnt[0] = 1
        dist[0] = 0
        MOD = 10**9+7  
        q = [(0,0)]
        while q:
            d, cur = heappop(q)
            if d > dist[cur]: continue
            if cur == n-1:
                return cnt[cur]
            for nxt, t in g[cur]:
                if dist[cur]+t <= dist[nxt]:
                    if dist[cur]+t < dist[nxt]:
                        cnt[nxt] = 0
                        dist[nxt] = dist[cur]+t 
                        heappush(q,(dist[nxt],nxt))
                    cnt[nxt] = (cnt[cur]+cnt[nxt])%MOD 
        return 0


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9+7
        dp = [0]*n 
        dist = [float('inf')]*n 
        dp[0] = 1
        dist[0] = 0
        pq = [(0,0)]
        g = defaultdict(list)
        mat = [[float('inf')]*n for _ in range(n)]
        for u, v, t in roads:
            g[u].append((v,t))
            g[v].append((u,t))
            mat[u][v] = t 
            mat[v][u] = t 
        while pq:
            d, cur = heapq.heappop(pq)
            if d > dist[cur]:
                continue
            for i in range(n):
                if dist[i]+mat[i][cur] <= dist[cur]:
                    dp[cur] += dp[i]
            dp[cur] %= MOD
            if cur == n-1:
                return dp[cur]
            for nxt, t in g[cur]:
                if dist[cur]+t < dist[nxt]:
                    dist[nxt] = dist[cur]+t 
                    heapq.heappush(pq,(dist[nxt],nxt))
        return -1 

