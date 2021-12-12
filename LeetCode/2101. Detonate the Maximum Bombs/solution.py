class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if j == i:
                    continue
                xj, yj, rj = bombs[j]
                if (xi-xj)**2+(yi-yj)**2 <= ri**2:
                    graph[i].append(j)

        res = 0
        for i in range(n):
            visited = [0]*n 
            q = deque()
            visited[i] = 1
            q.append(i)
            while q:
                cur = q.popleft()
                for nxt in graph[cur]:
                    if visited[nxt] == 0:
                        visited[nxt] = 1
                        q.append(nxt)
            res = max(res, sum(visited))
        return res

