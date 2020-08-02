class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dp = [0]*n
        dp[start] = 1
        q = [(-1,start)]
        g = defaultdict(list)
        for i, e in enumerate(edges):
            g[e[0]].append((e[1],succProb[i]))
            g[e[1]].append((e[0],succProb[i]))
        while q:
            prob, cur = heapq.heappop(q)
            # print(prob,cur,dp)
            prob = -prob
            if prob < dp[cur]:
                continue
            if cur == end:
                return prob 
            for nxt, w in g[cur]:
                if prob*w > dp[nxt]:
                    heapq.heappush(q,(-prob*w,nxt))
                    dp[nxt] = prob*w
        return dp[end]




# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
#         g, dq = defaultdict(list), deque([start])
#         for i, (a, b) in enumerate(edges):
#             g[a].append([b, i])
#             g[b].append([a, i])
#         p = [0.0] * n    
#         p[start] = 1.0
#         while dq:
#             cur = dq.popleft()
#             for neighbor, i in g.get(cur,[]):
#                 if p[cur] * succProb[i] > p[neighbor]:
#                     p[neighbor] = p[cur] * succProb[i]
#                     dq.append(neighbor)
#         return p[end]        