class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v, w in roads:
            g[u].append((v,w))
            g[v].append((u,w))
        def check(state):
            for u in range(n):
                if (state>>u)&1:
                    dist = [inf]*n  
                    dist[u] = 0
                    hq = [(0,u)]
                    while hq:
                        d, cur = heappop(hq)
                        if d > dist[cur]: continue
                        if d > maxDistance: return False
                        for nxt, w in g[cur]:
                            if (state>>nxt)&1 == 0: continue
                            if d+w < dist[nxt]:
                                dist[nxt] = d+w 
                                heappush(hq,(d+w,nxt))
                    for v in range(n):
                        if (state>>v)&1 and dist[v] == inf:
                            return False
            return True 

        return sum(check(s) for s in range(1<<n))