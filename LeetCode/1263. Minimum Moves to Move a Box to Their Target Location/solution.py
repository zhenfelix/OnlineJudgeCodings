# from typing import  List

# from collections import defaultdict
# import collections

# from pprint import pprint
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:



        def isconnect(obx, oby, ax, ay, bx, by):
            # print(xx,yy,px,py)
            q = collections.deque()
            visited = set()
            if 0 <= ax < n and 0 <= ay < m and grid[ax][ay] != '#':
                q.append((ax, ay))
                visited.add((ax, ay))

            while q:
                xx, yy = q.popleft()
                if (xx,yy) == (bx,by):
                    return True
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    if 0 <= xx+dx < n and 0 <= yy+dy < m and grid[xx+dx][yy+dy] != '#' and (xx,yy) != (obx,oby) and (xx+dx,yy+dy) not in visited:
                        q.append((xx+dx,yy+dy))
                        visited.add((xx+dx,yy+dy))
            return False

        n, m = len(grid), len(grid[0])
        # pprint(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'S':
                    player = (i,j)
                elif grid[i][j] == 'B':
                    box = (i,j)
                elif grid[i][j] == 'T':
                    target = (i,j)
        pq = collections.deque()
        configs = set()
        pq.append((box[0],box[1],player[0],player[1]))
        configs.add((box[0],box[1],player[0],player[1]))
        level = 0
        while pq:
            for _ in range(len(pq)):
                bx, by, px, py = pq.popleft()
                # print(bx, by, px, py)
                if (bx, by) == target:
                    return level
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    bx_, by_ = bx + dx, by + dy
                    if 0 <= bx_ < n and 0 <= by_ < m and grid[bx_][by_] != '#' and (bx_, by_, bx, by) not in configs and isconnect(bx, by, bx - dx, by - dy, px, py):
                        pq.append((bx_, by_, bx, by))
                        configs.add((bx_, by_, bx, by))
            level += 1

        return -1


import heapq

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "T":
                    target = (r, c)
                if grid[r][c] == "B":
                    start_box = (r, c)
                if grid[r][c] == "S":
                    start_person = (r, c)

        def heuristic(box):
            return 0
            # return abs(target[0] - box[0]) + abs(target[1] - box[1])

        def out_bounds(location):  # return whether the location is in the grid and not a wall
            r, c = location
            if r < 0 or r >= rows:
                return True
            if c < 0 or c >= cols:
                return True
            return grid[r][c] == "#"

        def isconnect(obs, a, b):
            q = collections.deque()
            covered = set()
            if not out_bounds(a):
                q.append(a)
                covered.add(a)
            while q:
                cur = q.popleft()
                if cur == b:
                    return True
                for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    nxt = (cur[0]+dr, cur[1]+dc)
                    if out_bounds(nxt) or nxt == obs or nxt in covered:
                        continue
                    q.append(nxt)
                    covered.add(nxt)
            return False

        visited = set()
        heap = [[heuristic(start_box), 0, start_person, start_box]]
        visited.add((start_person, start_box))

        while heap:
            _, moves, person, box = heapq.heappop(heap)
            if box == target:
                return moves

            for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                new_box = (box[0] + dr, box[1] + dc)
                if out_bounds(new_box) or (box, new_box) in visited or not isconnect(box,(box[0] - dr, box[1] - dc),person):
                    continue

                heapq.heappush(heap, [heuristic(new_box) + moves + 1, moves + 1, box, new_box])
                visited.add((box,new_box))


        return -1

        

# class Solution:
#     def minPushBox(self, grid: List[List[str]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "T":
#                     target = (r, c)
#                 if grid[r][c] == "B":
#                     start_box = (r, c)
#                 if grid[r][c] == "S":
#                     start_person = (r, c)
                    
#         def heuristic(box):
#             return abs(target[0] - box[0]) + abs(target[1] - box[1])
        
#         def out_bounds(location):  # return whether the location is in the grid and not a wall
#             r, c = location
#             if r < 0 or r >= rows:
#                 return True
#             if c < 0 or c >= cols:
#                 return True
#             return grid[r][c] == "#"
                        
#         heap = [[heuristic(start_box), 0, start_person, start_box]]
#         visited = set()
        
#         while heap:
#             _, moves, person, box = heapq.heappop(heap)
#             if box == target:
#                 return moves
#             if (person, box) in visited: # do not visit same state again
#                 continue
#             visited.add((person, box))
            
#             for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
#                 new_person = (person[0] + dr, person[1] + dc)
#                 if out_bounds(new_person):
#                     continue
                    
#                 if new_person == box:
#                     new_box = (box[0] + dr, box[1] + dc)
#                     if out_bounds(new_box):
#                         continue
#                     heapq.heappush(heap, [heuristic(new_box) + moves + 1, moves + 1, new_person, new_box])
#                 else:
#                     heapq.heappush(heap, [heuristic(box) + moves, moves, new_person, box]) # box remains same
        
#         return -1