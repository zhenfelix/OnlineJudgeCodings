class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        clock = 0
        visited = [-1]*n 
        ans = -1
        def bfs(root):
            nonlocal clock
            cur = root
            cnt = 0
            while cur != -1 and visited[cur] == -1:
                visited[cur] = clock
                clock += 1
                cur = edges[cur]
                cnt += 1
            if cur == -1 or visited[cur] < visited[root]:
                return 0
            return cnt-(visited[cur]-visited[root])

        for i in range(n):
            if visited[i] == -1:
                ans = max(ans, bfs(i))
        return ans 

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0]*n
        visited = [False]*n 
        for u, v in enumerate(edges):
            if v >= 0:
                indegree[v] += 1
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                visited[i] = True

        while q:
            cur = q.popleft()
            nxt = edges[cur]
            if nxt == -1:
                continue
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
                visited[nxt] = True

        def count(cur):
            cnt = 0
            while not visited[cur]:
                visited[cur] = True
                cnt += 1
                cur = edges[cur]
            return cnt
        ans = 0
        for i in range(n):
            if not visited[i]:
                ans = max(ans, count(i))
        return ans if ans != 0 else -1

