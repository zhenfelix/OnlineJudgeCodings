class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        m, n = len(grid), len(grid[0])
        sum = [[0] * (n + 1) for _ in range(m + 1)]
        diff = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):  # grid 的二维前缀和
                sum[i + 1][j + 1] = sum[i + 1][j] + sum[i][j + 1] - sum[i][j] + v

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 0:
                    x, y = i + stampHeight, j + stampWidth  # 注意这是矩形右下角横纵坐标都 +1 后的位置
                    if x <= m and y <= n and sum[x][y] - sum[x][j] - sum[i][y] + sum[i][j] == 0:
                        diff[i][j] += 1
                        diff[i][y] -= 1
                        diff[x][j] -= 1
                        diff[x][y] += 1  # 更新二维差分

        # 还原二维差分矩阵对应的计数矩阵，这里用滚动数组实现
        cnt, pre = [0] * (n + 1), [0] * (n + 1)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                cnt[j + 1] = cnt[j] + pre[j + 1] - pre[j] + diff[i][j]
                if cnt[j + 1] == 0 and v == 0:
                    return False
            cnt, pre = pre, cnt
        return True


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/stamping-the-grid/solution/wu-nao-zuo-fa-er-wei-qian-zhui-he-er-wei-zwiu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        n, m = len(grid), len(grid[0])
        # if stampHeight > n or stampWidth > m:
        #     return False
        blocks = [[0]*(m+1) for _ in range(n+1)]
        marks = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            pi = i-1
            for j in range(m):
                pj = j-1
                blocks[i][j] = grid[i][j]+blocks[pi][j]+blocks[i][pj]-blocks[pi][pj]
        for i in range(stampHeight-1,n):
            pi = i-stampHeight
            for j in range(stampWidth-1,m):
                pj = j-stampWidth
                if grid[i][j] == 0 and blocks[i][j]+blocks[pi][pj]-blocks[pi][j]-blocks[i][pj] == 0:
                    marks[i][j] = 1
        # print(marks)
        for i in range(n):
            pi = i-1
            for j in range(m):
                pj = j-1
                marks[i][j] += marks[pi][j]+marks[i][pj]-marks[pi][pj]
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 0:
                    i = min(x+stampHeight-1,n-1)
                    j = min(y+stampWidth-1,m-1)
                    pi = x-1
                    pj = y-1
                    if marks[i][j]+marks[pi][pj]-marks[pi][j]-marks[i][pj] == 0:
                        return False
        return True


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