from collections import deque

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        visited = set()
        q.append((0,0,-1))
        visited.add((0,0,-1))
        level = 0
        while q:
            m = len(q)
            for i in range(m):
                r, c, state = q.popleft()
                if (r,c,state) == (n-1,n-2,-1):
                    return level
                if state == -1:
                    if c+2 < n and grid[r][c+2] == 0 and (r,c+1,state) not in visited:
                        visited.add((r,c+1,state))
                        q.append((r,c+1,state))
                    if r+1 < n and grid[r+1][c] == 0 and grid[r+1][c+1] == 0:
                        if (r+1,c,state) not in visited:
                            visited.add((r+1,c,state))
                            q.append(r+1,c,state)
                        if (r,c,-state) not in visited:
                            visited.add((r,c,-state))
                            q.append((r,c,-state))
                else:
                    if r+2 < n and grid[r+2][c] == 0 and (r+1,c,state) not in visited:
                        visited.add((r+1,c,state))
                        q.append((r+1,c,state))
                    if c+1 < n and grid[r][c+1] == 0 and grid[r+1][c+1] == 0:
                        if (r,c+1,state) not in visited:
                            visited.add((r,c+1,state))
                            q.append((r,c+1,state))
                        if (r,c,-state) not in visited:
                            visited.add((r,c,-state))
                            q.append((r,c,-state))
            level += 1
        return -1
                

# class Solution:
#     def minimumMoves(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         horizontal, vertical = [[float('inf')]*n for _ in range(n)], [[float('inf')]*n for _ in range(n)]
#         horizontal[0][0] = 0
#         for r in range(n):
#             for c in range(n):
#                 if horizontal[r][c] > vertical[r][c] and r+1 < n and c+1 < n and grid[r][c+1] == 0 and grid[r+1][c+1] == 0:
#                     horizontal[r][c] = vertical[r][c] + 1
#                 elif horizontal[r][c] < vertical[r][c] and r+1 < n and c+1 < n and grid[r+1][c] == 0 and grid[r+1][c+1] == 0:
#                     vertical[r][c] = horizontal[r][c] + 1
#                 if c + 2 < n and grid[r][c+2] == 0:
#                     horizontal[r][c+1] = min(horizontal[r][c+1], horizontal[r][c]+1)
#                 if r + 1 < n and c+1 < n and grid[r+1][c] == 0 and grid[r+1][c+1] == 0:
#                     horizontal[r+1][c] = min(horizontal[r+1][c], horizontal[r][c]+1)
#                 if r + 2 < n and grid[r+2][c] == 0:
#                     vertical[r+1][c] = min(vertical[r+1][c], vertical[r][c]+1)
#                 if r + 1 < n and c+1 < n and grid[r][c+1] == 0 and grid[r+1][c+1] == 0:
#                     vertical[r][c+1] = min(vertical[r][c+1], vertical[r][c]+1)
#         print(horizontal)
#         print(vertical)
#         if horizontal[n-1][n-2] == float('inf'):
#             return -1
#         return horizontal[n-1][n-2]
                