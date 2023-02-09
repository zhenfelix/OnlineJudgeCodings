class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        tot = (1<<n)-1
        q = [(i,1<<i) for i in range(n)]
        visited = set(q)
        ans = 0
        while q:
            nq = []
            # print(q,ans)
            for i, s in q:
                if s == tot:
                    return ans 
                for j in graph[i]:
                    sj = s|(1<<j)
                    if (j,sj) not in visited:
                        visited.add((j,sj))
                        nq.append((j,sj))
            q = nq
            ans += 1
        return ans