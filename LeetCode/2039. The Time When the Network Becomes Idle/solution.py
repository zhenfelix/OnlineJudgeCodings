class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        dist = [float('inf')]*n 
        dist[0] = 0
        q = deque()
        q.append(0)
        step = 0
        while q:
            m = len(q)
            for _ in range(m):
                cur = q.popleft()
                for nxt in graph[cur]:
                    if step+1 < dist[nxt]:
                        dist[nxt] = step+1
                        q.append(nxt)
            step += 1
        res = 0
        for i in range(1,n):
            d = dist[i]*2
            res = max(res, d+(d-1)//patience[i]*patience[i])
        return res+1