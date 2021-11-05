class Solution:
    def secondMinimum(self, n, edges, time, change):
        D = [[] for _ in range(n + 1)]
        D[1] = [0]
        G, heap = defaultdict(list), [(0, 1)]
        
        for a, b in edges:
            G[a] += [b]
            G[b] += [a]

        while heap:
            min_dist, idx = heappop(heap)
            if idx == n and len(D[n]) == 2: return max(D[n])

            for neib in G[idx]:
                if (min_dist // change) % 2 == 0:
                    cand = min_dist + time
                else:
                    cand = ceil(min_dist/(2*change)) * (2*change) + time

                if not D[neib] or (len(D[neib]) == 1 and D[neib] != [cand]):
                    D[neib] += [cand]
                    heappush(heap, (cand, neib))


# TLE solution, construct 10000 nodes in a line, and set time = 1 and change = 1000

# class Solution:
#     def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
#         dist = defaultdict(int)
#         graph = defaultdict(list)
#         for a, b in edges:
#             a -= 1
#             b -= 1
#             graph[a].append(b)
#             graph[b].append(a)
#         q = [(0,0,0,0)]
#         dist[0,0,0] = 0
#         res = []
#         while q:
#             d, cur, remains, cycle = heapq.heappop(q)
#             # print(d,cur,remains,cycle)
#             for nxt in graph[cur]:
#                 nd = d + time
#                 green = ((nd//change)%2 == 0)
#                 nr = nd%change if green else 0
#                 nnd = nd if green else nd+(change-(nd%change))
#                 if nxt == n-1:
#                     if not res or res[-1] < nd:
#                         res.append(nd)
#                         if len(res) == 2:
#                             return res[-1]
#                 nc = cycle 
#                 if (nxt, nr, nc) in dist and nnd > dist[nxt,nr,nc]:
#                     nc += 1
#                 if nc > 1 or (nxt, nr, nc) in dist:
#                     continue
#                 dist[nxt,nr,nc] = nnd
#                 heapq.heappush(q,(nnd,nxt,nr,nc))
#         return -1

