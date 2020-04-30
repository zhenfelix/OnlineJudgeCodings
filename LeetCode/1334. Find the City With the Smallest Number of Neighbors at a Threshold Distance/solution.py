# class Solution:
#     def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
#         graph = defaultdict(list)
#         for a, b, w in edges:
#             graph[a].append((b,w))
#             graph[b].append((a,w))
#         def func(start):
#             dist = [float('inf')]*n
#             dist[start] = 0
#             q = [(0,start)]
#             heapq.heapify(q)
#             res = 0
#             while q:
#                 dcur, cur = heapq.heappop(q)
#                 if dist[cur] > distanceThreshold:
#                     break
#                 if dcur > dist[cur]:
#                     continue
#                 res += 1
#                 for nxt, d in graph[cur]:
#                     if dist[cur]+d < dist[nxt]:
#                         dist[nxt] = dist[cur]+d
#                         heapq.heappush(q,(dist[nxt],nxt))
#             return res, -start
#         # print([func(i) for i in range(n)])
#         return min(range(n), key=func)
            
            
class Solution:
#     def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
#         dp = defaultdict(int)
#         for i in range(n):
#             for j in range(n):
#                 if i != j:
#                     dp[-1,i,j] = float('inf')
#         for a, b, w in edges:
#             dp[-1,a,b] = w 
#             dp[-1,b,a] = w 
#         for k in range(n):
#             for i in range(n):
#                 for j in range(n):
#                     dp[k,i,j] = min(dp[k-1,i,j],dp[k-1,i,k]+dp[k-1,k,j])
#         return min(range(n), key = lambda x: (sum(dp[n-1,x,y] <= distanceThreshold for y in range(n)), -x))
        
        
    def findTheCity(self, n, edges, maxd):
        dis = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= maxd for d in dis[i]): i for i in range(n)}
        return res[min(res)]
                
                