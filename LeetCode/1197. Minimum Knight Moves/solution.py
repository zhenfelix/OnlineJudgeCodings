from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if y > x:
            x, y = y, x
        directions = [(2,1),(1,2),(-2,1),(-1,2),(2,-1),(1,-2),(-2,-1),(-1,-2)]
        q = deque()
        visited = set()
        q.append((0,0))
        level = 0
        while q:
            n = len(q)
            for _ in range(n):
                front = q.popleft()
                if front == (x,y):
                    return level
                for direction in directions:
                    x_next, y_next = front[0]+direction[0], front[1]+direction[1]
                    if (x_next,y_next) not in visited and -5 <= x_next <= 302 and -5 <= y_next <= x_next+5:
                        q.append((x_next,y_next))
                        visited.add((x_next,y_next))
            level += 1
        return -1


# class Solution(object):
#     memo = {(0, 0): 0}
#     queue = [(0, 0, 0)]
#     for x, y, d in queue:
#         for dx, dy in ((2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)):
#             nx = x+dx
#             ny = y+dy
#             if -5 <= nx <= 302 and -5 <= ny <= 302:
#                 if (nx, ny) not in memo:
#                     memo[nx,ny] = d+1
#                     queue.append((nx, ny, d+1))
       
#     def minKnightMoves(self, x, y):
#         x = abs(x)
#         y = abs(y)
#         return Solution.memo[x,y]