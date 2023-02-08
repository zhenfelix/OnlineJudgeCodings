class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        tot = n*m 
        parent = list(range(tot))
        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]
        def connect(u,v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return True
            parent[ru] = rv 
            return False

        for i in range(n):
            for j in range(m):
                if i and grid[i][j] == grid[i-1][j]:
                    if connect(i*m+j,(i-1)*m+j):
                        return True
                if j and grid[i][j] == grid[i][j-1]:
                    if connect(i*m+j,i*m+j-1):
                        return True
        return False


import sys
sys.setrecursionlimit(10**6)

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        seen = [[False]*m for _ in range(n)]

        def dfs(i,j,parent):
            
            seen[i][j] = True
            for ni, nj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni += i 
                nj += j
                if ni < 0 or ni >= n or nj < 0 or nj>= m or (ni,nj) == parent or grid[ni][nj] != grid[i][j]:
                    continue
                if seen[ni][nj] or dfs(ni,nj,(i,j)):
                    return True
            return False


        for r in range(n):
            for c in range(m):
                if not seen[r][c]:
                    if dfs(r,c,(-1,-1)):
                        return True
                    # print(r,c,seen,depth)
        return False