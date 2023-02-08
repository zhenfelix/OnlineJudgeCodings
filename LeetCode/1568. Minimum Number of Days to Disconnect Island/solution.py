class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dxy = [-1,0,1,0,-1]
        marks = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]: marks.append((i,j))

        def bfs(r, c):
            q = [(r,c)]
            visited = set([(r,c)])
            while q:
                nq = []
                for r, c in q:
                    for dr, dc in zip(dxy[:-1],dxy[1:]):
                        dr += r 
                        dc += c 
                        if 0 <= dr < n and 0 <= dc < m and grid[dr][dc] == 1 and (dr,dc) not in visited:
                            nq.append((dr,dc))
                            visited.add((dr,dc))
                q = nq 
            return visited

        if len(marks) <= 1:
            return len(marks)
        sr, sc = marks[0]
        seen = bfs(sr,sc)
        if len(seen) < len(marks):
            return 0
        for i, (r, c) in enumerate(marks):
            grid[r][c] = 0
            sr, sc = marks[i-1]
            seen = bfs(sr,sc)
            if len(seen) < len(marks)-1:
                return 1
            grid[r][c] = 1
        return 2


        

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def components():
            parent = [i for i in range(n*m)]

            def find(cur):
                if parent[cur] != cur:
                    parent[cur] = find(parent[cur])
                return parent[cur]
            def union(left,right):
                rl, rr = find(left), find(right)
                if rl != rr:
                    parent[rl] = rr 
                return 

            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 0: continue
                    for x, y in [(-1,0),(1,0),(0,-1),(0,1)]:
                        x += i
                        y += j
                        if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                            union(x*m+y, i*m+j)
            return len(set([find(i*m+j) for i in range(n) for j in range(m) if grid[i][j] == 1]))

        if components() > 1:
            return 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if components() > 1:
                        return 1
                    grid[i][j] = 1
        return 2