from functools import lru_cache
class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        ss, os, ms, ts = [], [], [], []
        os_mp = {}
        for i, row in enumerate(maze):
            for j, ch in enumerate(row):
                if ch == 'S':
                    ss.append((i, j))
                elif ch == 'O':
                    os_mp[i, j] = len(os)
                    os.append((i, j))
                elif ch == 'M':
                    # ms_mp[i, j] = len(ms)
                    ms.append((i, j))
                elif ch == 'T':
                    ts.append((i, j))

        ms = ms + ss 
        mo_dist = [[float('inf')] * len(os) for _ in range(len(ms))]
        mt_dist = [float('inf')] * len(ms)
        for i, m in enumerate(ms):
            visited = set([m])
            q = deque([m])
            step = 0
            while q:
                n = len(q)
                for _ in range(n):
                    r, c = q.popleft()
                    if maze[r][c] == "O":
                        mo_dist[i][os_mp[r, c]] = step
                    elif maze[r][c] == "T":
                        mt_dist[i] = step
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        rr, cc = r + dr, c + dc
                        if 0 <= rr < len(maze) and 0 <= cc < len(maze[0]) and (rr, cc) not in visited and maze[rr][cc] != "#":
                            visited.add((rr, cc))
                            q.append((rr, cc))
                step += 1

        if len(mo_dist) == 1:
            res = mt_dist[-1]
            return res if res != float('inf') else -1

        sz = len(ms)
        mm_dist = [[float('inf')]*sz for _ in range(sz)]
        for i in range(sz):
            for j in range(i,sz):
                mm_dist[i][j] = min(mo_dist[i][k]+mo_dist[j][k] for k in range(len(os)))
                mm_dist[j][i] = mm_dist[i][j]

        sz -= 1
        # dp = [[float('inf')]*(1<<sz) for _ in range(sz)]
        # q = deque()
        # for i in range(sz):
        #     q.append((i,1<<i))
        #     dp[i][1<<i] = mm_dist[i][-1]
        # while q:
        #     n = len(q)
        #     to_visit = set()
        #     for _ in range(n):
        #         i, cur = q.popleft()
        #         for j in range(sz):
        #             if not (cur & (1<<j)):
        #                 nxt = cur | (1<<j)
        #                 dp[j][nxt] = min(dp[j][nxt],mm_dist[i][j]+dp[i][cur])
        #                 to_visit.add((i,nxt))
        #     q = deque(list(to_visit))
        # res = min(dp[i][-1]+mt_dist[i] for i in range(sz))

        @lru_cache(None)
        def dfs(i,state):
            if 1<<i == state:
                return mm_dist[i][-1]
            return min(mm_dist[i][j]+dfs(j,state^(1<<i)) for j in range(sz) if (state & (1<<j)) and i != j)
        res = min(dfs(k,(1<<sz)-1)+mt_dist[k] for k in range(sz))
        return res if res != float('inf') else -1