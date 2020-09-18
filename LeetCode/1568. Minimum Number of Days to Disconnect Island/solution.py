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