class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = defaultdict(list)
        for a, b, w in edges:
            g[a].append((b,w+1))
            g[b].append((a,w+1))
        q = [(0,0)]
        visited = set()
        dist = [float('inf')]*N 
        dist[0] = 0
        while q:
            dd, cur = heapq.heappop(q)
            if dd > M:
                break
            if cur in visited:
                continue
            visited.add(cur)
            for nxt, w in g[cur]:
                if dd + w < dist[nxt]:
                    dist[nxt] = dd + w 
                    heapq.heappush(q, (dd+w, nxt))

        cnt = len(visited)
        for a, b, w in edges:
            tmp = 0
            tmp += max(0,M-dist[a])
            tmp += max(0,M-dist[b])
            cnt += min(w,tmp)
        return cnt
