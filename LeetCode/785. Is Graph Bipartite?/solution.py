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