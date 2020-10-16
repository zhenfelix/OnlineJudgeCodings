class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         def dfs(i,j,time):
#             visited.add((i,j))
#             if grid[i][j] > time:
#                 return False
#             if (i,j) == (n-1,n-1):
#                 return True
#             for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
#                 di += i 
#                 dj += j
#                 if 0 <= di < n and 0 <= dj < n and (di,dj) not in visited:
#                     if dfs(di,dj,time):
#                         return True
#             return False

#         lo, hi = 0, n*n 
#         while lo <= hi:
#             mid = (lo+hi)//2
#             visited = set()
#             if dfs(0,0,mid):
#                 hi = mid - 1
#             else:
#                 lo = mid + 1
#         return lo

    def swimInWater(self, grid):
        N, pq, seen, res = len(grid), [(grid[0][0], 0, 0)], set([(0, 0)]), 0
        while True:
            T, x, y = heapq.heappop(pq)
            res = max(res, T)
            if x == y == N - 1:
                return res
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if 0 <= i < N and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heapq.heappush(pq, (grid[i][j], i, j))