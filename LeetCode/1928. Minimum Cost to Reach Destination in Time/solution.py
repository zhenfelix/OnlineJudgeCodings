# class Solution:
#     def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
#         n = len(passingFees)
#         g = defaultdict(list)
#         dp = {(0,0): passingFees[0]}
#         q = [(passingFees[0],0,0)]
#         for a, b, t in edges:
#             g[a].append((b,t))
#             g[b].append((a,t))
#         while q:
#             cost, cur, time = heapq.heappop(q)
#             if time > maxTime or dp[cur,time] < cost:
#                 continue
#             if cur == n-1:
#                 return cost

#             for nxt, t in g[cur]:
#                 if cost+passingFees[nxt] < dp.get((nxt,time+t), float('inf')) and time+t <= maxTime:
#                     dp[nxt,time+t] = cost+passingFees[nxt]
#                     heapq.heappush(q, (dp[nxt,time+t],nxt,time+t))
#         return -1



# class Solution:
#     def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
#         n = len(passingFees)
        
#         g = [[] for i in range(n)]
#         for e in edges:
#             g[e[0]].append((e[1], e[2]))
#             g[e[1]].append((e[0], e[2]))
            
#         times = {}
        
#         pq = [(passingFees[0],0,0)]
        
#         while pq:
#             cost, node, time = heapq.heappop(pq)
            
#             if time > maxTime:
#                 continue
            
#             if node == n-1:
#                 return cost
            
#             if times.get(node, float('inf')) > time:
#                 times[node] = time
#                 for nbor, trip in g[node]:
#                     heapq.heappush(pq, (passingFees[nbor]+cost, nbor, time+trip))
            
#         return -1


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        g = defaultdict(list)
        times = {0: 0}
        q = [(passingFees[0],0,0)]
        for a, b, t in edges:
            g[a].append((b,t))
            g[b].append((a,t))
        while q:
            d, t, cur = heapq.heappop(q)
            if t > maxTime:
                continue
            if cur == n-1:
                return d

            for nxt, travel in g[cur]:
              
                if travel+t < times.get(nxt, float('inf')):
                    times[nxt] = travel+t 
                    heapq.heappush(q, (d+passingFees[nxt], times[nxt], nxt))
        return -1




class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        g = defaultdict(dict)
        dist = {0: 0}
        times = {0: 0}
        q = [(passingFees[0],0,0)]
        for a, b, t in edges:
            if t < g[a].get(b, float('inf')):
                g[a][b] = t  
            if t < g[b].get(a, float('inf')):
                g[b][a] = t 
        
        dp = [[float('inf')]*n for _ in range(maxTime+1)]
        dp[0][0] = passingFees[0]
        for t in range(maxTime):
            for cur in range(n):
                if dp[t][cur] == float('inf'):
                    continue
                # dp[t+1][cur] = min(dp[t+1][cur], dp[t][cur])
                for nxt, travel in g[cur].items():
                    if t+travel <= maxTime:
                        dp[t+travel][nxt] = min(dp[t+travel][nxt], dp[t][cur]+passingFees[nxt])
        res = min(dp[i][n-1] for i in range(maxTime+1))
        return res if res < float('inf') else -1

