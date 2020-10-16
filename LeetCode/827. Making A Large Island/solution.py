# class Solution:
#     def largestIsland(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         parent = [i for i in range(n*m)]
#         sz = [0]*(n*m)
#         self.res = 0
#         def find(x):
#             if x != parent[x]:
#                 parent[x] = find(parent[x])
#             return parent[x]
#         def union(x,y):
#             rx, ry = find(x), find(y)
#             if rx != ry:
#                 parent[rx] = ry
#                 sz[ry] += sz[rx]
                
#             return
#         def convert(ii, jj):
#             return ii*m + jj

#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 0:
#                     continue
#                 sz[convert(i,j)] = 1
#                 if i-1 >= 0 and grid[i-1][j] == 1:
#                     union(convert(i-1,j),convert(i,j))
#                 if j-1 >= 0 and grid[i][j-1] == 1:
#                     union(convert(i,j-1),convert(i,j))
#                 self.res = max(self.res, sz[find(convert(i,j))])
#         # print(self.res)
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1:
#                     continue
#                 candidate = set()
#                 for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
#                     di += i
#                     dj += j 
#                     if di < 0 or di >= n or dj < 0 or dj >= m:
#                         continue
#                     candidate.add(find(convert(di,dj)))
#                 self.res = max(self.res, sum([sz[idx] for idx in candidate])+1)
#         return self.res

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        sz = defaultdict(int)
        def dfs(x, y, color):
            grid[x][y] = color
            sz[color] += 1
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                dx += x
                dy += y 
                if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == 1:
                    dfs(dx, dy, color)


        idx, res = 1, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    idx += 1
                    dfs(i,j,idx)
                    res = max(res, sz[idx])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    candidate = set()
                    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        di += i 
                        dj += j 
                        if 0 <= di < n and 0 <= dj < m and grid[di][dj] > 1:
                            candidate.add(grid[di][dj])
                    res = max(res, sum([sz[c] for c in candidate])+1)
        return res
