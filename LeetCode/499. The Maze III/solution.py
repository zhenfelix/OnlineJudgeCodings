class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        n, m = len(maze), len(maze[0])
        mp = {'u':(-1,0), 'd':(1,0), 'l':(0,-1), 'r':(0,1)}
        rmp = dict()
        for k, v in mp.items():
            rmp[v] = k 
        dirs = "dlru"
        r, c = ball
        q = deque()
        visited = dict()
        for ch in dirs:
            q.append((0,(r,c),mp[ch]))
            visited[((r,c),mp[ch])] = ((r,c),mp[ch])

        def valid(rc,drc):
            r, c = rc
            dr, dc = drc
            return 0 <= r < n and 0 <= c < m and maze[r][c] == 0 and (rc,drc) not in visited
        def space(r, c):
            return 0 <= r < n and 0 <= c < m and maze[r][c] == 0
        def process(rc,drc):
            r, c = rc
            dr, dc = drc
            path = []
            while (rc,drc) != visited[(rc,drc)]:
                ch = rmp[drc]
                if not path or path[-1] != ch:
                    path.append(ch)
                rc,drc = visited[(rc,drc)]
            return ''.join(path[::-1])


        while q:
            d, (r,c), (dr,dc) = q.popleft()
            if (r,c) == (hole[0],hole[1]): 
                return process((r,c),(dr,dc))
            if valid((r+dr,c+dc),(dr,dc)):
                q.append((d+1,(r+dr,c+dc),(dr,dc)))
                visited[((r+dr,c+dc),(dr,dc))] = ((r,c),(dr,dc)) 
            elif not space(r+dr,c+dc):
                for ch in dirs:
                    dx, dy = mp[ch]
                    if valid((r+dx,c+dy),(dx,dy)):
                        q.append((d+1,(r+dx,c+dy),(dx,dy)))
                        visited[((r+dx,c+dy),(dx,dy))] = ((r,c),(dr,dc))
        return "impossible"



class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
                                                    
        directions = [(-1,0,'u'),(0,1,'r'),(0,-1,'l'),(1,0,'d')]    
                                                    # 定义上下左右四个方向和对应字符
        m = len(maze)                               # 获取矩阵大小
        n = len(maze[0])
        queue = [(ball[0],ball[1])]                 # 构造队列，并将起始位置包含其中
                                                    # distance 保存从起点到每个点的距离
                                                    # string 保存每个点对应的字符串
        distance = [[float('inf')]*n for _ in range(m)]
        string = [["impossible"]*n for _ in range(m)]
        distance[ball[0]][ball[1]] = 0              # 对起点的distance和string进行初始化
        string[ball[0]][ball[1]] = ""

        while queue:
            i,j = queue.pop(0)                      # 弹出坐标值i,j
            
            for dx,dy,letter in directions:         # 对四个方向进行遍历，letter保存了操作对应的字符
                x,y,step,word =i+dx,j+dy,distance[i][j],string[i][j]
                while 0<=x<m and 0<=y<n and maze[x][y] == 0 and (x-dx!=hole[0] or y-dy!=hole[1]):                                      
                                                    # 当x,y坐标合法，并且对应值为0
                                                    # 且没有越过hole时
                    x = x+dx                        # 继续前进，模拟小球的滚动过程
                    y = y+dy                        
                    step += 1                       # 记录步数

                x = x - dx
                y = y - dy

                if distance[x][y] > step or (distance[x][y]==step and word+letter<string[x][y]):           
                                                    # 如果起点到该点的距离比当前距离大
                                                    # 或者相等，但是字符串的字典序大
                                                    # 更新该距离和字符串，并将坐标加入队列
                    distance[x][y] = step
                    string[x][y] = word+letter
                    #print(x,y,string[x][y])   
                    if x!=hole[0] or y!=hole[1]:    # 当坐标不是hole坐标时
                        queue.append((x,y))         # 将其添加到队列中
                                           
        return string[hole[0]][hole[1]]


# 作者：heimisa000
# 链接：https://leetcode.cn/problems/the-maze-iii/solution/python3-bfsyan-du-you-xian-sou-suo-shuang-100da-li/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



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