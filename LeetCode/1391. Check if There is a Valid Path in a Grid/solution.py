# class Solution:
#     def hasValidPath(self, grid: List[List[int]]) -> bool:
#         def dfs(parent, cur):
#             if cur == (m-1,n-1):
#                 return True
#             r, c = cur
#             pr, pc = parent
#             if r < 0 or r >= m or c < 0 or c >= n:
#                 return False
#             state = grid[r][c]
#             nxt = (r, c+1)
#             if state in [1,4,6] and nxt != parent and 0 <= nxt[0] < m and 0 <= nxt[1] < n and grid[nxt[0]][nxt[1]] in [1,3,5] and dfs(cur,nxt):
#                 return True
#             nxt = (r+1,c)
#             if state in [2,3,4] and nxt != parent and 0 <= nxt[0] < m and 0 <= nxt[1] < n and grid[nxt[0]][nxt[1]] in [2,5,6] and dfs(cur,nxt):
#                 return True
#             nxt = (r,c-1)
#             if state in [1,3,5] and nxt != parent and 0 <= nxt[0] < m and 0 <= nxt[1] < n and grid[nxt[0]][nxt[1]] in [1,4,6] and dfs(cur,nxt):
#                 return True
#             nxt = (r-1,c)
#             if state in [2,5,6] and nxt != parent and 0 <= nxt[0] < m and 0 <= nxt[1] < n and grid[nxt[0]][nxt[1]] in [2,3,4] and dfs(cur,nxt):
#                 return True
#             return False
#         m, n = len(grid), len(grid[0])
#         return dfs((-1,-1),(0,0))
            
            
        
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]
        def union(a,b):
            if find(a) != find(b):
                parent[find(a)] = find(b)
            return
        
        n, m = len(grid), len(grid[0])
        parent = [i for i in range(n*m)]
        for r in range(n):
            for c in range(m):
                nr, nc = r, c+1
                if 0 <= nr < n and 0 <= nc < m and grid[r][c] in [1,4,6] and grid[nr][nc] in [1,3,5]:
                    union(r*m+c,nr*m+nc)
                nr, nc = r+1, c
                if 0 <= nr < n and 0 <= nc < m and grid[r][c] in [2,3,4] and grid[nr][nc] in [2,5,6]:
                    union(r*m+c,nr*m+nc)
                nr, nc = r, c-1
                if 0 <= nr < n and 0 <= nc < m and grid[r][c] in [1,3,5] and grid[nr][nc] in [1,4,6]:
                    union(r*m+c,nr*m+nc)
                nr, nc = r-1, c
                if 0 <= nr < n and 0 <= nc < m and grid[r][c] in [2,5,6] and grid[nr][nc] in [2,3,4]:
                    union(r*m+c,nr*m+nc)
        return find(0) == find(n*m-1)
                
            