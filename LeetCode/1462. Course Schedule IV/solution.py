class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre = [[False]*n for _ in range(n)]
        g = defaultdict(list)
        degree = Counter()
        for a, b in prerequisites:
            g[a].append(b)
            degree[b] += 1
        q = deque()
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            for nxt in g[cur]:
                for i in range(n):
                    if pre[i][cur]:
                        pre[i][nxt] = True
                pre[cur][nxt] = True
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    q.append(nxt)
        res = []
        for a, b in queries:
            res.append(pre[a][b])
        return res


class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        connected = [[False] * n for i in range(n)]

        for i, j in prerequisites:
            connected[i][j] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    connected[i][j] = connected[i][j] or (connected[i][k] and connected[k][j])

        return [connected[i][j] for i, j in queries]