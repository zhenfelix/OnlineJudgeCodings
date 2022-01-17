class Solution:
    def possibleToStamp(self, grid: List[List[int]], h: int, w: int) -> bool:
        n, m = len(grid), len(grid[0])
        if h > n or w > m:
            return sum(sum(g) for g in grid) == n*m
        occupies = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                occupies[i][j] = occupies[i-1][j]+occupies[i][j-1]-occupies[i-1][j-1]+grid[i][j]
        # for s in occupies:
        #     print(s)
        stamps = [[0]*m for _ in range(n)]
        for i in range(n-h+1):
            for j in range(m-w+1):
                if grid[i][j] == 1:
                    continue
                # print(i,j,occupies[i+h-1][j+w-1],occupies[i+h-1][j-1],occupies[i-1][j+w-
                # 1],occupies[i-1][j-1])
                if occupies[i+h-1][j+w-1]-occupies[i+h-1][j-1]-occupies[i-1][j+w-1]+occupies[i-1][j-1] == 0:
                    stamps[i][j] = 1
        # for s in stamps:
        #     print(s)
        sums = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                sums[i][j] = stamps[i][j]+sums[i-1][j]+sums[i][j-1]-sums[i-1][j-1]
                # print(i,j,sums[i])
                ii = max(i-h,-1)
                jj = max(j-w,-1)
                if grid[i][j] == 0 and sums[i][j]+sums[ii][jj]-sums[ii][j]-sums[i][jj] <= 0:
                    return False
            # print(i)
            # print(sums[i])
        return True



drc = [(-1,0),(1,0),(0,-1),(0,1)]
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        n, m = len(grid), len(grid[0])
        sums = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                sums[i][j] = grid[i][j]+sums[i-1][j]+sums[i][j-1]-sums[i-1][j-1]
        cnt = 0
        def bfs(r, c):
            if grid[r][c] == 1:
                return
            grid[r][c] = 1
            q = deque()
            q.append((r,c))
            while q:
                rr, cc = q.popleft()
                for dr, dc in drc:
                    dr += rr 
                    dc += cc
                    if r-stampHeight < dr <= r and c-stampWidth < dc <= c and grid[dr][dc] == 0:
                        grid[dr][dc] = 1
                        q.append((dr,dc))
            return

        for i in range(stampHeight-1, n):
            for j in range(stampWidth-1, m):
                if sums[i][j]-sums[i-stampHeight][j]-sums[i][j-stampWidth]+sums[i-stampHeight][j-stampWidth] == 0:
                    bfs(i,j)
        return n*m == sum(sum(g) for g in grid)