class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        ans = 0
        for g in set(group):
            g_ans = 0
            def dfs(u, p):
                nonlocal g_ans
                c = 1 if group[u] == g else 0
                d = 0
                for v in adj[u]:
                    if v != p:
                        sc, sd = dfs(v, u)
                        if sc:
                            td = sd + sc
                            g_ans += d * sc + td * c
                            c += sc
                            d += td
                return c, d
            dfs(0, -1)
            ans += g_ans
        return ans