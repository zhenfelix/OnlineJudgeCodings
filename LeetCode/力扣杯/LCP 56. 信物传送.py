class Solution:
    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        n, m = len(matrix), len(matrix[0])
        q = deque()
        q.append((start[0],start[1],0))
        dist = [[n+m]*m for _ in range(n)]
        dist[start[0]][start[1]] = 0
        dxy = [-1,0,1,0,-1]
        dirs = "^>v<"
        while q:
            x, y, d = q.popleft()
            if x == end[0] and y == end[1]:
                return d 
            if d > dist[x][y]:
                continue
            for i, (dx, dy) in enumerate(zip(dxy[:-1],dxy[1:])):
                dx += x 
                dy += y
                if dx < 0 or dx >= n or dy < 0 or dy >= m:
                    continue
                if dirs[i] == matrix[x][y]:
                    if d < dist[dx][dy]:
                        dist[dx][dy] = d
                        q.appendleft((dx,dy,d))
                else:
                    if d + 1 < dist[dx][dy]:
                        dist[dx][dy] = d+1
                        q.append((dx,dy,d+1))
        return -1




class Solution:
    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        n, m = len(matrix), len(matrix[0])
        q = deque()
        q.append((start[0],start[1]))
        dist = [[n+m]*m for _ in range(n)]
        dist[start[0]][start[1]] = 0
        visited = [[False]*m for _ in range(n)]
        dxy = [-1,0,1,0,-1]
        dirs = "^>v<"
        while q:
            x, y = q.popleft()
            if x == end[0] and y == end[1]:
                return dist[x][y]
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            for i, (dx, dy) in enumerate(zip(dxy[:-1],dxy[1:])):
                dx += x 
                dy += y
                if dx < 0 or dx >= n or dy < 0 or dy >= m:
                    continue
                if dirs[i] == matrix[x][y]:
                    dist[dx][dy] = min(dist[dx][dy], dist[x][y])
                    q.appendleft((dx,dy))                        
                else:
                    dist[dx][dy] = min(dist[dx][dy], dist[x][y]+1)
                    q.append((dx,dy))                        
        return -1

