# class Solution:
#     def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
#         n, m = len(grid), len(grid[0])
#         upleft = [[0]*m for _ in range(n)]
#         for i in range(n):
#             for j in range(m):
#                 upleft[i][j] = grid[i][j]
#                 if i and j:
#                     upleft[i][j] += upleft[i-1][j-1]
#         upright = [[0]*m for _ in range(n)]
#         for i in range(n):
#             for j in range(m)[::-1]:
#                 upright[i][j] = grid[i][j]
#                 if i and j+1 < m:
#                     upright[i][j] += upright[i-1][j+1]
#         downright = [[0]*m for _ in range(n)]
#         for i in range(n)[::-1]:
#             for j in range(m)[::-1]:
#                 downright[i][j] = grid[i][j]
#                 if i+1 < n and j+1 < m:
#                     downright[i][j] += downright[i+1][j+1]
#         downleft = [[0]*m for _ in range(n)]
#         for i in range(n)[::-1]:
#             for j in range(m):
#                 downleft[i][j] = grid[i][j]
#                 if i+1 < n and j:
#                     downleft[i][j] += downleft[i+1][j-1]

#         def valid(x,y):
#             return 0 <= x < n and 0 <= y < m 
        
#         # print(upleft)
#         # print(upright)
#         # print(downright)
#         # print(downleft)
#         res = set()
#         for i in range(n):
#             for j in range(m):
#                 res.add(grid[i][j])
#                 for k in range(1,max(n,m)):
#                     if any(not valid(i+di,j+dj) for di, dj in [(0,k),(k,0),(0,-k),(-k,0)]):
#                         break
#                     cur = 0
#                     cur += upleft[i][j+k] - upleft[i-k][j]
#                     cur += upright[i+k][j] - upright[i][j+k]
#                     cur += downright[i][j-k] - downright[i+k][j]
#                     cur += downleft[i-k][j] - downleft[i][j-k]
#                     res.add(cur)
#         res = sorted(list(res), reverse = True)
#         return res[:3]



class Solution:
    def getBiggestThree(self, grid):
        m, n, heap = len(grid), len(grid[0]), []
        
        def update(heap, num):
            if num not in heap:
                heappush(heap, num)
                if len(heap) > 3: heappop(heap)
            return heap
        
        for num in chain(*grid): update(heap, num)
          
        @lru_cache(None)
        def dp(i, j, dr):
            if not 0 <= i < n or not 0 <= j < m: return 0
            return dp(i-1, j+dr, dr) + grid[j][i]
        
        for q in range(1, (1 + min(m, n))//2):
            for i in range(q, n - q):
                for j in range(q, m - q):
                    p1 = dp(i + q, j, -1) - dp(i, j - q, -1)
                    p2 = dp(i - 1, j + q - 1, -1) - dp(i - q - 1, j - 1, -1)
                    p3 = dp(i, j - q, 1) - dp(i - q, j, 1)
                    p4 = dp(i + q - 1, j + 1, 1) - dp(i - 1, j + q + 1, 1)
                    update(heap, p1 + p2 + p3 + p4)

        return sorted(heap)[::-1]