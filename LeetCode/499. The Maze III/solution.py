# from collections import defaultdict

# class Solution:
#     def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
#         n, m = len(maze), len(maze[0])
#         ball = (ball[0],ball[1])
#         hole = (hole[0],hole[1])
#         ans = [float('inf'),"impossible"]
#         # directions = {'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
#         directions = {'d':(1,0),'l':(0,-1),'r':(0,1),'u':(-1,0)}
#         visited = defaultdict(int)
#         visited[ball] = 0
#         def dfs(cur,cnt,path):
#             # print(cur)
#             if cnt > ans[0]:
#                 return
#             for k, v in directions.items():
#                 # print(k,v)
#                 x, y = cur[0], cur[1]
#                 while 0 <= x+v[0] < n and 0 <= y+v[1] < m and maze[x+v[0]][y+v[1]] != 1:
#                     x += v[0]
#                     y += v[1]
#                     if (x,y) == hole:
#                         delta = max(abs(x-cur[0]),abs(y-cur[1]))
#                         if cnt+delta < ans[0]:
#                             ans[0] = cnt+delta
#                             ans[1] = path+k
#                         elif cnt+delta == ans[0] and path+k < ans[1]:
#                             ans[1] = path+k
#                         return
#                 if max(abs(x-cur[0]),abs(y-cur[1]))  > 0 and cnt+max(abs(x-cur[0]),abs(y-cur[1])) < visited.get((x,y),float('inf')):
#                 # if max(abs(x-cur[0]),abs(y-cur[1]))  > 0 and cnt+max(abs(x-cur[0]),abs(y-cur[1])) <= visited.get((x,y),float('inf')):
#                     visited[(x,y)] = cnt+max(abs(x-cur[0]),abs(y-cur[1]))
#                     dfs((x,y),cnt+max(abs(x-cur[0]),abs(y-cur[1])),path+k)
                
#             return

#         dfs(ball,0,"")
#         return ans[1]

import heapq

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        n, m = len(maze), len(maze[0])
        ball = (ball[0],ball[1])
        hole = (hole[0],hole[1])
        directions = {'u':(-1,0),'d':(1,0),'l':(0,-1),'r':(0,1)}
        expanded = set()
        q = [(0,"",ball)]
        # limit = float('inf')
        while q:
            cnt, path, cur = heapq.heappop(q)
            if cur == hole:
                return path
            # if cur in expanded or cnt == limit:
            if cur in expanded:
                continue
            expanded.add(cur)            
            for k, v in directions.items():
                x, y = cur[0], cur[1]
                while 0 <= x+v[0] < n and 0 <= y+v[1] < m and maze[x+v[0]][y+v[1]] == 0:
                    x += v[0]
                    y += v[1]
                    if (x,y) == hole:
                        # limit = min(limit, cnt+max(abs(x-cur[0]),abs(y-cur[1])))
                        break
                if max(abs(x-cur[0]),abs(y-cur[1])) > 0:
                    heapq.heappush(q,(cnt+max(abs(x-cur[0]),abs(y-cur[1])), path+k,(x,y)))

        return "impossible"