class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
        res = float('inf')
        for u, v in edges:
            ws = g[u]&g[v]
            if ws:
                tmp = min(len(g[w])-2 for w in ws)
                res = min(res, tmp + len(g[u]) + len(g[v]) - 4)
        return res if res < float('inf') else -1