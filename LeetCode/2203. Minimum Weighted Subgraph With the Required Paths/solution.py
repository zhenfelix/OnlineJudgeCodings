class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def dijstra(start, adj):
            dp = [float('inf')]*n
            dp[start] = 0
            q = [(0,start)]
            while q:
                dist, cur = heapq.heappop(q)
                if dist > dp[cur]:
                    continue
                for nxt, w in adj[cur]:
                    if dist+w < dp[nxt]:
                        dp[nxt] = dist+w 
                        heapq.heappush(q, (dp[nxt],nxt))
            return dp[:]

        g = defaultdict(list)
        rg = defaultdict(list)
        for f, t, w in edges:
            g[f].append((t,w))
            rg[t].append((f,w))
        dp_src1 = dijstra(src1,g)
        dp_src2 = dijstra(src2,g)
        dp_dest = dijstra(dest,rg)
        res = float('inf')
        for i in range(n):
            res = min(res, dp_src1[i]+dp_src2[i]+dp_dest[i])
        return res if res < float('inf') else -1