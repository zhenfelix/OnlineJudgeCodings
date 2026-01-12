import sys
sys.setrecursionlimit(600000)

class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        d = [(1 if x else -1) for x in good]

        def dfs1(u, p):
            for v in g[u]:
                if v != p:
                    dfs1(v, u)
                    if d[v] > 0: d[u] += d[v]

        def dfs2(u, p):
            for v in g[u]:
                if v != p:
                    up = d[u] - (d[v] if d[v] > 0 else 0)
                    if up > 0: d[v] += up
                    dfs2(v, u)

        dfs1(0, -1)
        dfs2(0, -1)
        return d