class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        g = defaultdict(list)
        for u, v, w in edges:
            u -= 1
            v -= 1
            g[u].append((v,w))
            g[v].append((u,w))
        dp = [0]*n
        dp[n-1] = 1
        dist = [float('inf')]*n
        dist[n-1] = 0
        q = [(0,n-1)]
        while q:
            d, cur = heapq.heappop(q)
            if d > dist[cur]:
                continue
            for nxt, w in g[cur]:
                if dist[nxt] < dist[cur]:
                    dp[cur] += dp[nxt]
                    dp[cur] %= MOD
                if dist[cur] + w < dist[nxt]:
                    dist[nxt] = dist[cur] + w 
                    heapq.heappush(q,(dist[nxt],nxt))
            if cur == 0:
                return dp[0]
        return -1
