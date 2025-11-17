class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        idx = [[0] * n for _ in range(m)]
        cnt_l = sx = sy = 0
        for i, row in enumerate(classroom):
            for j, b in enumerate(row):
                if b == 'L':
                    idx[i][j] = 1 << cnt_l  # 给垃圾分配编号（提前计算左移）
                    cnt_l += 1
                elif b == 'S':
                    sx, sy = i, j
        if cnt_l == 0:
            return 0

        DIRS = (-1, 0), (1, 0), (0, -1), (0, 1)
        vis = [[[[False] * (1 << cnt_l) for _ in range(energy + 1)] for _ in range(n)] for _ in range(m)]
        vis[sx][sy][energy][0] = True
        q = [(sx, sy, energy, 0)]

        full_mask = (1 << cnt_l) - 1
        ans = 0
        while q:
            tmp = q
            q = []
            for x, y, e, mask in tmp:
                if mask == full_mask:  # 所有垃圾收集完毕
                    return ans
                if e == 0:  # 没能量了
                    continue
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                        new_e = energy if classroom[nx][ny] == 'R' else e - 1
                        new_mask = mask | idx[nx][ny]  # 添加垃圾（没有垃圾时 mask 不变）
                        if not vis[nx][ny][new_e][new_mask]:
                            vis[nx][ny][new_e][new_mask] = True
                            q.append((nx, ny, new_e, new_mask))
            ans += 1
        return -1

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimum-moves-to-clean-the-classroom/solutions/3690747/bfs-by-endlesscheng-rpk6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。