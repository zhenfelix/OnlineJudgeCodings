class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        if matrix[-1][-1] == '#':
            return -1

        m, n = len(matrix), len(matrix[0])
        pos = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, c in enumerate(row):
                if c.isupper():
                    pos[c].append((i, j))

        DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = 0
        q = deque([(0, 0)])

        while q:
            x, y = q.popleft()
            d = dis[x][y]

            if x == m - 1 and y == n - 1:  # 到达终点
                return d

            c = matrix[x][y]
            if c in pos:
                # 使用所有传送门
                for px, py in pos[c]:
                    if d < dis[px][py]:
                        dis[px][py] = d
                        q.appendleft((px, py))
                del pos[c]  # 避免重复使用传送门

            # 下面代码和普通 BFS 是一样的
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#' and d + 1 < dis[nx][ny]:
                    dis[nx][ny] = d + 1
                    q.append((nx, ny))

        return -1

作者：灵茶山艾府
链接：https://leetcode.cn/problems/grid-teleportation-traversal/solutions/3679952/0-1-bfspythonjavacgo-by-endlesscheng-8nj9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        n, m = len(matrix), len(matrix[0])
        visited = [[0]*m for _ in range(n)]
        doors = defaultdict(list)
        for i in range(n):
            for j in range(m):
                ch = matrix[i][j]
                if ch not in ".#":
                    doors[ch].append((i,j))

        q = deque()
        dr, dc= 0, 0 
        if 0 <= dr < n and 0 <= dc < m and not visited[dr][dc]:
            ch = matrix[dr][dc]
            candidates = []
            if ch in doors:
                candidates = doors[ch]
            elif ch == '.':
                candidates = [(dr,dc)]
            for nr, nc in candidates:
                visited[nr][nc] = 1
                q.append((nr,nc,0))
        dxy = [-1,0,1,0,-1]
        # print(doors)
        while q:
            r, c, d = q.popleft()
            # print(r,c,d)
            if (r,c) == (n-1,m-1): return d 
            for dr, dc in zip(dxy[:-1],dxy[1:]):
                dr += r 
                dc += c 
                if 0 <= dr < n and 0 <= dc < m and not visited[dr][dc]:
                    ch = matrix[dr][dc]
                    candidates = []
                    if ch in doors:
                        candidates = doors[ch]
                    elif ch == '.':
                        candidates = [(dr,dc)]
                    for nr, nc in candidates:
                        visited[nr][nc] = 1
                        q.append((nr,nc,d+1))
        return -1



