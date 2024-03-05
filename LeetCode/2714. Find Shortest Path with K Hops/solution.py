class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        g = defaultdict(list)
        for u,v,w in edges:
            g[u].append((v,w))
            g[v].append((u,w))
        dp = [inf]*n 
        for _ in range(k+1):
            hq = []
            ndp = [inf]*n 
            ndp[s] = 0
            for i in range(n):
                for j, w in g[i]:
                    ndp[i] = min(ndp[i],dp[j])
                hq.append((ndp[i],i))
            heapify(hq)
            while hq:
                dist, i = heappop(hq)
                if dist > ndp[i]: continue
                for j, w in g[i]:
                    if dist+w < ndp[j]:
                        ndp[j] = dist+w 
                        heappush(hq,(ndp[j],j))
            dp = ndp 
        return dp[d]