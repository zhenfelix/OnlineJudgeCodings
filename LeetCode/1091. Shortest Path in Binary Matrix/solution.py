# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         q=collections.deque()
#         n=len(grid)
#         if n==0:
#             return -1
#         visited=[[0]*n for _ in range(n)]
#         dist=1
#         visited[0][0]==1
#         if grid[0][0]==0:
#             q.appendleft((0,0))
#         adj=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
#         while len(q)>0:
#             q_size=len(q)
#             for _ in range(q_size):
#                 tmp=q.pop()
#                 if tmp==(n-1,n-1):
#                     return dist
#                 for k in range(8):
#                     r=tmp[0]+adj[k][0]
#                     c=tmp[1]+adj[k][1]
#                     if 0<=r<n and 0<=c<n and visited[r][c]==0 and grid[r][c]==0:
#                         visited[r][c]=1
#                         q.appendleft((r,c))
#             dist+=1
#         return -1
                        
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = [(0, 0, 1)]
        for i, j, d in q:
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    if x == n-1 and y == n-1: return d+1
                    grid[x][y] = 1
                    q.append((x, y, d+1))
        return -1