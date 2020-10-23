# import math

# class Solution:
#     def maxDistance(self, grid: List[List[int]]) -> int:
#         n = len(grid)
        
#         leftup = [[0]*n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     ans = math.inf
#                     if i > 0:
#                         ans = min(ans, leftup[i-1][j]+1)
#                     if j > 0:
#                         ans = min(ans, leftup[i][j-1]+1)
#                     leftup[i][j] = ans
        
#         rightup = [[0]*n for _ in range(n)]
#         for i in range(n):
#             for j in range(n-1,-1,-1):
#                 if grid[i][j] == 0:
#                     ans = math.inf
#                     if i > 0:
#                         ans = min(ans, rightup[i-1][j]+1)
#                     if j < n-1:
#                         ans = min(ans, rightup[i][j+1]+1)
#                     rightup[i][j] = ans
                        
#         leftdown = [[0]*n for _ in range(n)]
#         for i in range(n-1,-1,-1):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     ans = math.inf
#                     if i < n-1:
#                         ans = min(ans, leftdown[i+1][j]+1)
#                     if j > 0:
#                         ans = min(ans, leftdown[i][j-1]+1)
#                     leftdown[i][j] = ans
                    
#         rightdown = [[0]*n for _ in range(n)]
#         for i in range(n-1,-1,-1):
#             for j in range(n-1,-1,-1):
#                 if grid[i][j] == 0:
#                     ans = math.inf
#                     if i < n-1:
#                         ans = min(ans, rightdown[i+1][j]+1)
#                     if j < n-1:
#                         ans = min(ans, rightdown[i][j+1]+1)
#                     rightdown[i][j] = ans
        
#         ans = -1
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     ans = max(ans, min(leftup[i][j], rightup[i][j], leftdown[i][j], rightdown[i][j]))
#         if ans == math.inf:
#             return -1
#         return ans




class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def neighbor(i,j):
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                di += i
                dj += j
                if 0 <= di < n and 0 <= dj < n:
                    yield di, dj


        q = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r,c))
        step = 0
        while q:
            m = len(q)
            step += 1
            for _ in range(m):
                r, c = q.popleft()
                for nr, nc in neighbor(r,c):
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr,nc))
        return step-1 if step > 1 else -1