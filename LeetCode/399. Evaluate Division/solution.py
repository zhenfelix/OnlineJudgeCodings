# 参考
# 2307. Check for Contradictions in Equations
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        parent = dict()
        dp = dict()
        def find(u):
            if u not in parent or parent[u] == u:
                parent[u] = u 
                return u 
            parent[u] = find(parent[u])
            return parent[u]

        def connect(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
            return

        for r, (a,b) in zip(values,equations):
            connect(a,b)
            g[a].append((b,1/r))
            g[b].append((a,r))

        def dfs(cur, v):
            if cur in dp:
                return
            dp[cur] = v 
            for nxt, r in g[cur]:
                dfs(nxt, v*r)
            return

        for a, b in equations:
            dfs(a, 1)

        ans = []
        for a, b in queries:
            ra, rb = find(a), find(b)
            if ra != rb or a not in dp:
                ans.append(-1)
            else:
                ans.append(dp[a]/dp[b])
        return ans


