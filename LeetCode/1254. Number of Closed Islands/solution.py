# 小心短路运算

# from pprint import pprint
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m:
                return False
            if grid[x][y] == 1:
                return True
            flag = True
            grid[x][y] = 1
            # pprint(grid)
            # pprint("\n")
            for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                flag = dfs(x+dx, y+dy) and flag # 小心短路运算

            return flag

        # def bfs(x, y):
        #     flag = True
        #     q = collections.deque()
        #     q.append((x,y))
        #     # grid[x][y] = 1
        #     while q:
        #         x, y = q.popleft()
        #         if x < 0 or x >= n or y < 0 or y >= m:
        #             flag = False
        #             continue
        #         if grid[x][y] == 1:
        #             continue
        #         grid[x][y] = 1
        #         for dx, dy in [(0,-1),(0,1),(1,0),(-1,0)]:
        #             q.append((x+dx, y+dy))
        #     return flag



        if not grid:
            return 0
        n , m = len(grid), len(grid[0])
        cnt = 0
        # pprint(grid)
        # pprint("\n")
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and dfs(i,j):
                    cnt += 1
                    # pprint(grid)
                    # print(i,j)
        
        return cnt



class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # def dfs(x, y):
        #     if x < 0 or x >= n or y < 0 or y >= m:
        #         return False
        #     if grid[x][y] == 1:
        #         return True
        #     flag = True
        #     grid[x][y] = 1
        #     for dx, dy in [(0,-1),(0,1),(1,0),(-1,0)]:
        #         flag = flag and dfs(x+dx, y+dy)
        #     return flag

        def bfs(x, y):
            flag = True
            q = collections.deque()
            q.append((x,y))
            # grid[x][y] = 1
            while q:
                x, y = q.popleft()
                if x < 0 or x >= n or y < 0 or y >= m:
                    flag = False
                    continue
                if grid[x][y] == 1:
                    continue
                grid[x][y] = 1
                for dx, dy in [(0,-1),(0,1),(1,0),(-1,0)]:
                    q.append((x+dx, y+dy))
            return flag



        if not grid:
            return 0
        n , m = len(grid), len(grid[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and bfs(i,j):
                    cnt += 1
                    # print(grid)
                    # print(i,j)
        return cnt
