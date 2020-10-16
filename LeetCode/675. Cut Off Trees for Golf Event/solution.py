# class Solution:
#     def cutOffTree(self, forest: List[List[int]]) -> int:
#         n, m = len(forest), len(forest[0])
#         def bfs(sx,sy,ex,ey):
#             q = deque()
#             visited = set()
#             q.append((sx,sy,0))
#             visited.add((sx,sy))
#             while q:
#                 cx, cy, step = q.popleft()
#                 if  (cx,cy) == (ex,ey):
#                     return step
#                 for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#                     dx += cx
#                     dy += cy
#                     if 0 <= dx < n and 0 <= dy < m and (dx,dy) not in visited and forest[dx][dy] > 0:
#                         q.append((dx,dy,step+1))
#                         visited.add((dx,dy))
#             return float('inf')

#         hq = []
#         for i in range(n):
#             for j in range(m):
#                 if forest[i][j] > 1:
#                     hq.append((forest[i][j],i,j))
#         ans, x, y = 0, 0, 0
#         heapq.heapify(hq)
#         while hq:
#             _, nx, ny = heapq.heappop(hq)
#             ans += bfs(x,y,nx,ny)
#             if ans == float('inf'):
#                 return -1
#             x, y = nx, ny
#         return ans

class Solution:
    def cutOffTree(self, forest):

        # Add sentinels (a border of zeros) so we don't need index-checks later on.
        forest.append([0] * len(forest[0]))
        for row in forest:
            row.append(0)

        # Find the trees.
        trees = [(height, i, j)
                 for i, row in enumerate(forest)
                 for j, height in enumerate(row)
                 if height > 1]

        # Can we reach every tree? If not, return -1 right away.
        queue = [(0, 0)]
        reached = set()
        for i, j in queue:
            # print(i,j)
            if (i, j) not in reached and forest[i][j]:
                reached.add((i, j))
                queue += (i+1, j), (i-1, j), (i, j+1), (i, j-1)
        if not all((i, j) in reached for (_, i, j) in trees):
            return -1

        # Distance from (i, j) to (I, J).
        def hadlock(i, j, I, J):
            now, soon = [(i, j)], []
            expanded = set()
            manhattan = abs(i - I) + abs(j - J)
            detours = 0
            while True:
                if not now:
                    now, soon = soon, []
                    detours += 1
                i, j = now.pop()
                if (i, j) == (I, J):
                    return manhattan + 2 * detours
                if (i, j) not in expanded:
                    expanded.add((i, j))
                    for i, j, closer in (i+1, j, i < I), (i-1, j, i > I), (i, j+1, j < J), (i, j-1, j > J):
                        if forest[i][j]:
                            (now if closer else soon).append((i, j))


        def astar(i, j, I, J):
            def h(ii, jj):
                return abs(ii-I) + abs(jj-J)
            expanded = set()
            q = [(h(i,j),i,j)]
            g = {(i,j): 0}
            while q:
                cf, ci, cj = heapq.heappop(q)
                if (ci,cj) == (I,J):
                    return cf 
                if (ci,cj) not in expanded:
                    expanded.add((ci,cj))
                    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        di += ci 
                        dj += cj
                        if forest[di][dj] > 0 and g.get((di,dj),float('inf')) > g.get((ci,cj),float('inf')) + 1:
                            g[(di,dj)] = g[(ci,cj)] + 1
                            heapq.heappush(q,(g[(di,dj)]+h(di,dj),di,dj))
                            # if (di,dj) in expanded:
                            #     expanded.remove((di,dj))
            return float('inf')



        # Sum the distances from one tree to the next (sorted by height).
        trees.sort()
        return sum(astar(i, j, I, J) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees))