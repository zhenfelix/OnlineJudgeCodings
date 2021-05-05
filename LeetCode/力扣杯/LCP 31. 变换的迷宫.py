
class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        q = deque()
        T = len(maze)
        n, m = len(maze[0]), len(maze[0][0])
        # visited = set()
        t = 0
        for i in range(n):
            for j in range(m):
                q.append((0,0,0,0))
        while q:
            sz = len(q)
            visited = set()
            for _ in range(sz):
                row, col, tmp, per = q.popleft()
                if (row,col) == (n-1,m-1):
                    return True
                if n-1-row+m-1-col > T-1-t:
                    continue
                if t+1 < T:
                    for dr, dc in [(0,0),(0,1),(0,-1),(1,0),(-1,0)]:
                        dr += row
                        dc += col
                        if dr < 0 or dr >= n or dc < 0 or dc >= m:
                            continue
                        if (dr,dc) != (row,col) and per == 1:
                            per = 2
                        if maze[t+1][dr][dc] == ".":
                            # if (dr,dc) != (row,col) and per == 1:
                            #     per = 2
                            if (dr,dc,tmp,per) not in visited:
                                visited.add((dr,dc,tmp,per))
                                q.append((dr,dc,tmp,per))
                        else:
                            if per == 1 and (dr,dc,tmp,per) not in visited:
                                visited.add((dr,dc,tmp,per))
                                q.append((dr,dc,tmp,per))
                            if tmp == 0 and (dr,dc,1,per) not in visited:
                                visited.add((dr,dc,1,per))
                                q.append((dr,dc,1,per))
                            if per == 0 and (dr,dc,tmp,1) not in visited:
                                visited.add((dr,dc,tmp,1))
                                q.append((dr,dc,tmp,1))

                            
            t += 1
 
        return False