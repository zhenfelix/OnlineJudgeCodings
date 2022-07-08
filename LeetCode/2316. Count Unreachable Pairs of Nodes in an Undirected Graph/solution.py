class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        visited = [False]*n 
        def bfs(cur):
            q = deque()
            q.append(cur)
            visited[cur] = True
            cnt = 1
            while q:
                cur = q.popleft()
                for nxt in g[cur]:
                    if not visited[nxt]:
                        q.append(nxt)
                        visited[nxt] = True
                        cnt += 1
            return cnt 
        arr = []
        for i in range(n):
            if not visited[i]:
                arr.append(bfs(i))
        if len(arr) == 1:
            return 0
        ans = 0
        for a in arr:
            ans += a*(n-a)
        return ans//2