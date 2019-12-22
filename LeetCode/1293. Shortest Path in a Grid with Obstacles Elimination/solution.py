# class Solution:
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         n, m = len(grid), len(grid[0])
#         q = collections.deque()
#         visited = set()
#         q.append((0,0,k,0))
#         visited.add((0,0,k,0))
#         while q:
#             i,j,limit,step = q.popleft()
#             if (i,j) == (n-1,m-1):
#                 return step
#             for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#                 x, y = i+dx, j+dy
#                 if 0 <= x < n and 0 <= y < m:
#                     new_limit = limit-grid[x][y]
#                     if new_limit < 0 or (x,y,new_limit,step+1) in visited:
#                         continue
#                     q.append((x,y,new_limit,step+1))
#                     visited.add((x,y,new_limit,step+1))
#         return -1
    
# class Solution:
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         n, m = len(grid), len(grid[0])
#         q = collections.deque()
#         visited = set()
#         q.append((0,0,k,0))
#         visited.add((0,0,k))
#         while q:
#             i,j,limit,step = q.popleft()
#             if (i,j) == (n-1,m-1):
#                 return step
#             for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#                 x, y = i+dx, j+dy
#                 if 0 <= x < n and 0 <= y < m:
#                     new_limit = limit-grid[x][y]
#                     if new_limit < 0 or (x,y,new_limit) in visited:
#                         continue
#                     q.append((x,y,new_limit,step+1))
#                     visited.add((x,y,new_limit))
#         return -1

from collections import deque
class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        s = [[[False]*(k+1) for j in range(m)] for i in range(n)]
        q = deque()
        def consider(x, y, z, d):
            if x<0 or x>=n or y<0 or y>=m: return
            z += grid[x][y]
            if z>k or s[x][y][z]: return
            s[x][y][z] = True
            q.append((x, y, z, d))
        consider(0, 0, 0, 0)
        while q:
            x, y, z, d = q.popleft()
            consider(x+1, y, z, d+1)
            consider(x-1, y, z, d+1)
            consider(x, y+1, z, d+1)
            consider(x, y-1, z, d+1)
            if x==n-1 and y==m-1: return d
        return -1