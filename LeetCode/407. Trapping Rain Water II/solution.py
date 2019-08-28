# import heapq

# class Solution:
#     def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
#         n = len(heightMap)
#         if n == 0:
#             return 0
#         m = len(heightMap[0])
#         if m == 0:
#             return 0

#         pq = [] 
#         visited = set()
#         i, j = 0, 0
#         while j < m:
#             pq.append((heightMap[i][j],i,j))
#             visited.add((i,j))
#             j += 1
#         i, j = i+1, j-1
#         while i < n:
#             pq.append((heightMap[i][j],i,j))
#             visited.add((i,j))
#             i += 1
#         i, j = i-1, j-1
#         while j >= 0:
#             pq.append((heightMap[i][j],i,j))
#             visited.add((i,j))
#             j -= 1
#         i, j = i-1, j+1
#         while i > 0:
#             pq.append((heightMap[i][j],i,j))
#             visited.add((i,j))
#             i -= 1
        
#         heapq.heapify(pq)
#         H, res = 0, 0
#         dx, dy = [0,0,-1,1], [-1,1,0,0]
#         while len(pq) > 0:
#             cur = heapq.heappop(pq)
#             H = max(H, cur[0])
#             res += H - cur[0]
#             for k in range(4):
#                 x, y = dx[k]+cur[1], dy[k]+cur[2]
#                 if (x,y) not in visited and x >= 0 and x < n and y >= 0 and y < m:
#                     heapq.heappush(pq, (heightMap[x][y],x,y))
#                     visited.add((x,y))
#         return res


import heapq
from collections import deque

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        n = len(heightMap)
        if n == 0:
            return 0
        m = len(heightMap[0])
        if m == 0:
            return 0

        pq = [] 
        visited = set()
        i, j = 0, 0
        while j < m:
            pq.append((heightMap[i][j],i,j))
            visited.add((i,j))
            j += 1
        i, j = i+1, j-1
        while i < n:
            pq.append((heightMap[i][j],i,j))
            visited.add((i,j))
            i += 1
        i, j = i-1, j-1
        while j >= 0:
            pq.append((heightMap[i][j],i,j))
            visited.add((i,j))
            j -= 1
        i, j = i-1, j+1
        while i > 0:
            pq.append((heightMap[i][j],i,j))
            visited.add((i,j))
            i -= 1
        
        heapq.heapify(pq)
        H, res = 0, 0
        dx, dy = [0,0,-1,1], [-1,1,0,0]
        q = deque()
        while len(pq) > 0:
            
            q.append(heapq.heappop(pq))
            while len(q) > 0:
                cur = q.popleft()
                H = max(H, cur[0])
                res += H - cur[0]
                for k in range(4):
                    x, y = dx[k]+cur[1], dy[k]+cur[2]
                    if (x,y) not in visited and x >= 0 and x < n and y >= 0 and y < m:
                        if heightMap[x][y] > H:
                            heapq.heappush(pq, (heightMap[x][y],x,y))
                        else:
                            q.append((heightMap[x][y],x,y))                       
                        visited.add((x,y))
       
        return res

# Mixture of priority and normal queue to speed up bfs

# Priority queue using min-heap to find the minimum heihgt at current boundary, from this point onwards, bfs neighboring area using normal queue while adding those higher than current minimum height to the outer priority queue to construct new boundary and others to the normal queue to contain water with current minimum height.

