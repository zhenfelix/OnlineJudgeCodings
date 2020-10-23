class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        state = [0]*n
        q = deque()
        for i in range(n):
            if state[i] != 0:
                continue
            q.append(i)
            state[i] = -1
            while q:
                cur = q.popleft()
                for nxt in graph[cur]:
                    if state[nxt] == 0:
                        state[nxt] = state[cur]*(-1)
                        q.append(nxt)
                    elif state[nxt]*state[cur] > 0:
                        return False
        return True

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(N)]
        for a, b in dislikes:
            g[a-1].append(b-1)
            g[b-1].append(a-1)
        return self.isBipartite(g)
        