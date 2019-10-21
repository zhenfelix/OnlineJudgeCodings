from collections import deque

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        n, m = len(maze), len(maze[0])
        maze = [[1]+row+[1] for row in maze]
        maze = [[1]*(m+2)]+maze+[[1]*(m+2)]
        start = (start[0]+1,start[1]+1)
        destination = (destination[0]+1,destination[1]+1)
        q = deque()
        visited = set()
        q.append(start)
        visited.add(start)
        while q:
            cur = q.popleft()
            if cur == destination:
                return True
            for dx, dy in zip([-1,1,0,0],[0,0,-1,1]):
                x, y = cur[0], cur[1]
                while maze[x+dx][y+dy] != 1:
                    x += dx
                    y += dy
                if (x,y) not in visited:
                    q.append((x,y))
                    visited.add((x,y))
        return False