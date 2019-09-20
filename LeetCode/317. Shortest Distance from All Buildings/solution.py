from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        building_cnt = 0
        m = len(grid)
        n = len(grid[0])
        
        cnts = [[0] * n for _ in range(m)]
        dists = copy.deepcopy(cnts)
        # dists = [[0] * n for _ in range(m)]
        
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    vis = [[0] * n for _ in range(m)]
                    q = deque()
                    q.append([i,j])
                    building_cnt += 1
                    level = 1
                    while len(q) != 0:
                        # print('cur queue: ', q)
                        for k in range(len(q)):
                            prev_x, prev_y = q.popleft()
                            for d in dirs:
                                x = prev_x + d[0]
                                y = prev_y + d[1]
                                if (0 <= x < m) and (0 <= y < n) and (grid[x][y] == 0) and (not vis[x][y]):
                                    vis[x][y] = 1
                                    cnts[x][y] += 1
                                    dists[x][y] += level
                                    q.append([x,y])
                        level += 1
        # print("num of building: ", building_cnt)
        # print("dists: ", dists)
        # print("cnts: ", cnts)
        
        ans = float("inf")
        for i in range(m):
            for j in range(n):
                if cnts[i][j] == building_cnt:
                    ans = min(ans, dists[i][j])
        return ans if ans != float("inf") else -1