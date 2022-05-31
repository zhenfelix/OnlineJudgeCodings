class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        graph = defaultdict(list)
        for f, t in edges:
            graph[t].append(f)

        def bfs(i):
            visited = set()
            q = deque([i])
            visited.add(i)
            while q:
                cur = q.popleft()
                if cur != i:
                    ans[i].append(cur)
                for nxt in graph[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
            return

        for i in range(n):
            bfs(i)

        return [sorted(a) for a in ans] 