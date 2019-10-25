# from collections import deque, defaultdict

# class Solution:
#     def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
#         n, m = len(maze), len(maze[0])
#         maze = [[1]+row+[1] for row in maze]
#         maze = [[1]*(m+2)]+maze+[[1]*(m+2)]
#         start = (start[0]+1,start[1]+1)
#         destination = (destination[0]+1,destination[1]+1)
#         q = deque()
#         q.append(start)
#         visited = defaultdict(int)
#         visited[start] = 0
#         while q:
#             cur = q.popleft()
#             dis = visited[cur]
#             # print(cur,dis)
#             if cur == destination:
#                 # visited[destination] = min(visited.get(destination,float('inf')), dis)
#                 continue
#             for dx, dy in zip([-1,1,0,0],[0,0,-1,1]):
#                 x, y = cur[0], cur[1]
#                 while maze[x+dx][y+dy] != 1:
#                     x += dx
#                     y += dy
#                 delta = max(abs(x-cur[0]),abs(y-cur[1]))
#                 if dis+delta < visited.get((x,y),float('inf')):
#                     q.append((x,y))
#                     visited[(x,y)] = dis+delta

#         if visited.get(destination,float('inf')) < float('inf'):
#             return visited[destination ]
#         return -1

import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        ans = set()
        m, n = len(maze), len(maze[0])
        heap = [[0, start[0], start[1]]]
        while heap:
            dis, x, y = heapq.heappop(heap)
            if (x, y) in ans:
                continue
            ans.add((x,y))
            if [x, y] == destination:
                return dis
            for dx, dy in [[-1,0],[1,0],[0,1],[0,-1]]:
                nx, ny = x, y
                while 0<=nx<m and 0<=ny<n and maze[nx][ny] == 0:
                    nx, ny = nx+dx, ny+dy
                nx, ny = nx-dx, ny-dy
                if (nx, ny) not in ans:
                    heapq.heappush(heap, [dis+abs(nx-x)+abs(ny-y), nx, ny])
        return -1